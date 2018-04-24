#!/usr/bin/python

import time
import sys
from EpicsCA import *

X_start = float(sys.argv[1])
X_end = float(sys.argv[2])
X_step = float(sys.argv[3])
Y_start = float(sys.argv[4])
Y_end = float(sys.argv[5])
Y_step = float(sys.argv[6])


EXPOSURE_TIME = 0.5 #s
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
 
def getI2():
  status = caput(SHUTTER, shutter_open, wait=1)
  time.sleep(0.05) # Wait 50 ms for slow shutter to open fully
  # start scaler 
  status = caput(SCALER_SET_TIME, EXPOSURE_TIME, wait=1)
  status = caput(SCALER_START, 1)
  time.sleep(EXPOSURE_TIME+0.1)   # Wait for scaler to complete
  status = caput(SHUTTER, shutter_close, wait=1)
  # read scaler values
  I0 = caget(SCALER_I0)
  I1 = caget(SCALER_I1)
  I2 = caget(SCALER_I2)
  I3 = caget(SCALER_I3)
  return I2

#---main---
# step scan with defined grid points in space
posX = X_start
while (posX <= X_end):
  posY = Y_start
  while (posY <= Y_end):
    MoveToXY(posX, posY)
    I2value = getI2()  
    print '%.03f, %.03f, %d' %(posX, posY, I2value)
    posY += Y_step
  posX += X_step
