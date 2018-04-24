#!/usr/bin/python

import time
import sys
import epics

print '\n\n\n'
print 'Usage: python scanMixer.py 18ID:n:m15 I3 start end step'
print '\n\n\n'
motorPV = sys.argv[1]
pindiode = sys.argv[2]
start = float(sys.argv[3])
end = float(sys.argv[4])
step = float(sys.argv[5])

EXPOSURE_TIME = 0.2 #s

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
 
def getDark():
  status = epics.caput(SHUTTER, shutter_close, wait=1)
  time.sleep(0.05) # Wait 50 ms for slow shutter to close
 
  # start scaler 
  status = epics.caput(SCALER_SET_TIME, EXPOSURE_TIME, wait=1)
  status = epics.caput(SCALER_START, 1)
  time.sleep(EXPOSURE_TIME+0.1)   # Wait for scaler to complete
  # read scaler values
  I0 = epics.caget(SCALER_I0)
  I1 = epics.caget(SCALER_I1)
  I2 = epics.caget(SCALER_I2)
  I3 = epics.caget(SCALER_I3)
  return {'I0':I0, 'I1':I1, 'I2':I2, 'I3':I3}
  
def getIonChamber():
  # start scaler 
  status = epics.caput(SCALER_SET_TIME, EXPOSURE_TIME, wait=1)
  status = epics.caput(SCALER_START, 1)
  time.sleep(EXPOSURE_TIME+0.1)   # Wait for scaler to complete
  # read scaler values
  I0 = epics.caget(SCALER_I0)
  I1 = epics.caget(SCALER_I1)
  I2 = epics.caget(SCALER_I2)
  I3 = epics.caget(SCALER_I3)
  return {'I0':I0, 'I1':I1, 'I2':I2, 'I3':I3}
  
import numpy as np
import os
import sys

# step scan with defined grid points in space
motor_position = []
incident_I = []
knifeedge_I = []


raw_input('Please check SHUTTER OPEN switch on XiA, is it off? Type y to continue...')
print 'Taking dark background ...'
I_dark = getDark()

print 'Move motor to the start position %.03f mm...' %start
MoveToX(start)

# Open shutter 
status = epics.caput(SHUTTER, shutter_open, wait=1)
time.sleep(0.05) # Wait 50 ms for slow shutter to open fully
print 'Open shutter' 

posX = start
while (posX <= end):
  MoveToX(posX)
  I_values = getIonChamber()
  motor_position.append(posX)
  incident_I.append(I_values['I0'] - I_dark['I0'])
  knifeedge_I.append(I_values[pindiode] - I_dark[pindiode])  
  print '%.03f, %d, %d' %(posX, I_values['I0'] - I_dark['I0'], I_values[pindiode] - I_dark[pindiode])
  posX += step

# Close shutter
status = epics.caput(SHUTTER, shutter_close, wait=1)
print 'Close shutter' 

normalized_I = np.divide(knifeedge_I, incident_I)

import pylab as pl

pl.figure(1)
pl.plot(motor_position, normalized_I, 'o')
pl.title('Knife-edge step scan I1/I0')
pl.show()

logName = 'mixer-scan.log'

import datetime
str_dt = datetime.datetime.now().strftime("%Y%m%d-%H%M")
scanName = str_dt  + '.h5' 
remark = raw_input('Add remark to the current scan (max. 80 characters):\n')

with open(logName, 'a') as flog:
    flog.write('%s, %s, [%.03f, %.03f] %.03f, %s\n' %(scanName, motorPV, start, end, step, remark))


raw_scan = np.array(zip(motor_position, incident_I, knifeedge_I))
h5remark = np.array(remark)

import h5py

with h5py.File(scanName, 'w') as fscan:
  dset_raw = fscan.create_dataset("raw-scan", data=raw_scan)
  dset_raw.attrs['column names'] = ['motor position (mm)', 'incident I', 'knife edge I']
  dset_remark = fscan.create_dataset("remark", data=h5remark)
print 'File %s saved!' %scanName

scantxt = str_dt + '.txt'
np.savetxt(scantxt, raw_scan)
print 'File %s saved!' %scantxt

###########How to read out the h5 data with python
#f = h5py.File(scanName, 'r')
#raw = np.array(f['raw-scan'])
#print raw
#remark = np.array(f['remark'])
#print remark
################################################
