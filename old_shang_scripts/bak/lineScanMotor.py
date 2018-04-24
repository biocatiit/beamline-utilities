#!/usr/bin/python

import time
import sys
import epics

motorPV = sys.argv[1]
start = float(sys.argv[2])
end = float(sys.argv[3])
step = float(sys.argv[4])


EXPOSURE_TIME = 0.5 #s

def MoveToX(posX):
  status = epics.caput(motorPV + '.VAL', posX, wait=True)

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
 
def getI2():
  status = epics.caput(SHUTTER, shutter_open, wait=1)
  time.sleep(0.05) # Wait 50 ms for slow shutter to open fully
  # start scaler 
  status = epics.caput(SCALER_SET_TIME, EXPOSURE_TIME, wait=1)
  status = epics.caput(SCALER_START, 1)
  time.sleep(EXPOSURE_TIME+0.1)   # Wait for scaler to complete
  status = epics.caput(SHUTTER, shutter_close, wait=1)
  # read scaler values
  I0 = epics.caget(SCALER_I0)
  I1 = epics.caget(SCALER_I1)
  I2 = epics.caget(SCALER_I2)
  I3 = epics.caget(SCALER_I3)
  return I2

#---main---
# step scan with defined grid points in space
posX = start
while (posX <= end):
  MoveToX(posX)
  I2value = getI2()  
  print '%.03f, %d' %(posX, I2value)
  posX += step
