#!/usr/bin/python

import time
import sys
from EpicsCA import *

scanName = sys.argv[1]

N_FRAMES = 10
EXPOSURE_TIME = 0.5 #s
FRAME_PERIOD = 0.6 #s
# Newport PV names
NewportY = '18ID:n:m16.'
NewportX = '18ID:n:m15.'
npX_Position = NewportX + 'VAL'
npY_Position = NewportY + 'VAL'

def MoveToXY(posX, posY):
  status = caput(npX_Position, posY, wait=1)
  status = caput(npY_Position, posX, wait=1)

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
  time.sleep(totalTime+2)   # Wait for detector&scaler to complete
  status = caput(SHUTTER, shutter_close, wait=1)
  # read scaler values
  I0 = caget(SCALER_I0)
  I1 = caget(SCALER_I1)
  I2 = caget(SCALER_I2)
  I3 = caget(SCALER_I3)
  print I0, I1, I2, I3
  # save intensity values
  file = open(image_prefix, "w")
  file.write('counter time: %d' %totalTime)
  file.write('%d, %d, %d, %d' %(I0, I1, I2, I3))
  file.close()

#---main---
# step scan with defined grid points in space

for line in file('stepscan.positions'):
  xy = line.split()
  x = float(xy[0])
  y = float(xy[1])
  print '(%.03f,%.03f) requested.' %(x, y) 
  MoveToXY(x, y)
  print 'Position (%.03f, %.03f) reached.' %(caget(npX_Position), caget(npY_Position)) 
  print 'start Pilatus 1M ...'
  tifName = '%s_%.03fy%.03f' %(scanName, x, y)
  doPilatus(tifName)
  print 'Pilatus 1M complete!\n'
