#!/usr/bin/python

import time
from EpicsCA import *

scanName = sys.argv[1]
X_start = float(sys.argv[2])
X_end = float(sys.argv[3])
X_step = float(sys.argv[4])
Y_start = float(sys.argv[5])
Y_end = float(sys.argv[6])
Y_step = float(sys.argv[7])
print X_start, X_end, X_step, Y_start, Y_end, Y_step

N_FRAMES =1
EXPOSURE_TIME = 1 #s
FRAME_PERIOD = 1.01 #s
# Newport PV names
NewportY = '18ID:n:m16.'
NewportX = '18ID:n:m15.'
npX_Position = NewportX + 'VAL'
npY_Position = NewportY + 'VAL'

def MoveToXY(posX, posY):
  status = caput(npX_Position, posX, wait=1)
  status = caput(npY_Position, posY, wait=1)

# Shutter PV name
SHUTTER = '18ID:bo0:ch6'
shutter_open = 0
shutter_close = 1

# APS ring current
RING_CURRENT = 'S:SRcurrentAI'

# Joerger scaler PV names
SCALER_SET_TIME = '18ID:scaler2.TP'
SCALER_START = '18ID:scaler2.CNT'
SCALER_I0 = '18ID:scaler2.S3'
SCALER_I1 = '18ID:scaler2.S4'
SCALER_I2 = '18ID:scaler2.S5'
SCALER_I3 = '18ID:scaler2.S6'
 

# Pilatus 1M PV names
PV_PILATUS = '18IDpil1M:cam1:'
filename_pv = PV(PV_PILATUS+'FileName')
frameno_pv  = PV(PV_PILATUS+'FileNumber')
acquire_pv  = PV(PV_PILATUS+'Acquire')
acqmode_pv  = PV(PV_PILATUS+'AcquireMode')
expp_pv     = PV(PV_PILATUS+'AcquirePeriod')
expt_pv     = PV(PV_PILATUS+'AcquireTime')
nimg_pv     = PV(PV_PILATUS+'NumImages')

def doPilatus(image_prefix):
  filename_pv.put(image_prefix)
  frameno_pv.put(1)
  acqmode_pv.put(0)
  expp_pv.put(FRAME_PERIOD) # acquire period
  expt_pv.put(EXPOSURE_TIME) # exposure time
  nimg_pv.put(N_FRAMES)    # number of frames

  totalTime = N_FRAMES*FRAME_PERIOD

  status = caput(SHUTTER, shutter_open, wait=1)
  time.sleep(0.05) # Wait 50 ms for slow shutter to open fully
  # start scaler 
  status = caput(SCALER_SET_TIME, totalTime, wait=1)
  status = caput(SCALER_START, 1)
  acquire_pv.put(1) # Start Pilatus 1M
  time.sleep(totalTime+0.2)   # Wait for detector&scaler to complete
  status = caput(SHUTTER, shutter_close, wait=1)
  # read scaler values
  I0 = caget(SCALER_I0)
  I1 = caget(SCALER_I1)
  I2 = caget(SCALER_I2)
  I3 = caget(SCALER_I3)
  print I0, I1, I2, I3
  # save intensity values
  file = open(image_prefix, "w")
  file.write('counter time: %d\n' %totalTime)
  file.write('%d, %d, %d, %d\n' %(I0, I1, I2, I3))
  file.close()

#---main---
# step scan with defined a grid boundary and step size in space
posX = X_start
while (posX <= X_end):
  posY = Y_start
  while (posY <= Y_end):
    print '(%.03f,%.03f) requested.' %(posX, posY) 
    MoveToXY(posX, posY)
    print 'Position (%.03f, %.03f) reached.' %(caget(npX_Position), caget(npY_Position)) 
    tifName = '%s_x%.03fy%.03f' %(scanName, posX, posY)
    print 'start Pilatus 1M ... for prefix ' + tifName
    doPilatus(tifName)
    print 'Pilatus 1M complete!\n'
    posY += Y_step
  posX += X_step
