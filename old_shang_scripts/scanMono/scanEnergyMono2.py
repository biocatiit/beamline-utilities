#!/usr/bin/python

import time
import sys
import epics

motorPV = '18ID:MO2:E'
start = float(sys.argv[1])
end = float(sys.argv[2])
step = float(sys.argv[3])

EXPOSURE_TIME = 0.5 #s

def MoveToX(posX):
  status = epics.caput(motorPV + ':RqsPos', posX, wait=True, timeout=60) 
  # wait=True does not work
  E = float(epics.caget(motorPV + ':ActPos'))
  while (abs(E - posX) > 0.0009):
    time.sleep(0.1)
    E = float(epics.caget(motorPV + ':ActPos'))
    #print E, posX, abs(posX - E)
  time.sleep(0.5)
  #print 'Energy %.03f keV reached!' %E

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
  status = epics.caput(SCALER_START, 1, wait=True, timeout=60)
  # time.sleep(EXPOSURE_TIME+0.1)   # Wait for scaler to complete
  # read scaler values
  I0 = epics.caget(SCALER_I0)
  I1 = epics.caget(SCALER_I1)
  I2 = epics.caget(SCALER_I2)
  I3 = epics.caget(SCALER_I3)
  return {'I0':I0, 'I1':I1, 'I2':I2, 'I3':I3}
  
def getIonChamber():
  # start scaler 
  status = epics.caput(SCALER_SET_TIME, EXPOSURE_TIME, wait=1)
  status = epics.caput(SCALER_START, 1, wait=True, timeout=60)
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
energy = []
incident_I = []
knifeedge_I = []

# Take dark counts
I_dark = getDark()
print 'Taking dark background ...'

print 'Set Energy to start value %.03f keV...' %start
MoveToX(start)

# Open shutter 
status = epics.caput(SHUTTER, shutter_open, wait=1)
time.sleep(0.05) # Wait 50 ms for slow shutter to open fully
print 'Open shutter'
time.sleep(3) # wait 3 s for feedback 

# Scan the given Mono energy PV
posX = start
while (posX <= end):
  MoveToX(posX)
  I_values = getIonChamber()
  energy.append(posX)
  incident_I.append(I_values['I0'] - I_dark['I0'])
  knifeedge_I.append(I_values['I1'] - I_dark['I1'])  
  print '%.03f, %d, %d' %(posX, I_values['I0'] - I_dark['I0'], I_values['I1'] - I_dark['I1'])
  posX += step

# Close shutter
status = epics.caput(SHUTTER, shutter_close, wait=1)

normalized_I = np.divide(incident_I, knifeedge_I)
normalized_I[np.isnan(normalized_I)] = 0
diff_I = np.diff(normalized_I) # take derivative
diff_I[np.isnan(diff_I)] = 0   # convert NaNs to 0

xx = energy[:-1]
yy = diff_I

from numpy import pi, exp
def Gaussian(x, A, mean, sigma):
    return A*exp(-(x-mean)**2/(2.0*sigma**2))
# FWHM = 2*sqrt(2*ln2)*sigma ~ 2.3548*sigma

init_vals = [0.2, 11.8, 0.001]
from scipy.optimize import curve_fit
best_vals, covar = curve_fit(Gaussian, xx, yy, p0=init_vals)
print best_vals
print 'Gaussian center = %.03f +- %.03f keV' %(best_vals[1], best_vals[2]*1.1774)

import pylab as pl
pl.figure(1)
pl.subplot(211)
pl.plot(energy, normalized_I, 'o')
pl.title('Monochromator energy scan I1/I0')
#pl.ylim([-0.2, 1.2])

pl.subplot(212)
pl.plot(xx, yy, 'o')
pl.plot(xx, Gaussian(xx, best_vals[0], best_vals[1], best_vals[2]))
pl.title('Gaussian center = %.03f +- %.03f keV' %(best_vals[1], best_vals[2]*1.1774))
pl.show()

logName = 'mono-energy-scan.log'

import datetime
scanName = datetime.datetime.now().strftime("%Y%m%d-%H%M") + '.h5'
remark = raw_input('Add remark to the current scan (max. 80 characters):\n')

with open(logName, 'a') as flog:
    flog.write('%s, %s, [%.03f, %.03f] %.03f, %.03f+-%.03f keV, %s\n' %(scanName, motorPV, start, end, step, best_vals[1], best_vals[2], remark))

raw_scan = np.array(zip(energy, incident_I, knifeedge_I))
derivative = np.array(zip(xx, yy))
h5remark = np.array(remark)
h5fit= np.array(best_vals)

import h5py

with h5py.File(scanName, 'w') as fscan:
  dset_raw = fscan.create_dataset("raw-scan", data=raw_scan)
  dset_raw.attrs['column names'] = ['energy (keV)', 'incident I', 'knife edge I']
  dset_derivative = fscan.create_dataset("derivative", data=derivative)
  dset_derivative.attrs['column names'] = ['energy (keV)', 'derivative of normalized I']
  dset_remark = fscan.create_dataset("remark", data=h5remark)
  dset_fwhm = fscan.create_dataset("Gaussian fit", data=h5fit)
print 'File %s saved!' %scanName
