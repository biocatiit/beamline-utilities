#!/usr/bin/env python

import argparse
import numpy as np
import h5py
import matplotlib.pyplot as plt
import scipy.interpolate

parser = argparse.ArgumentParser(description='Replot the beamsize from a saved scan.')
parser.add_argument('name', help='The filename to plot.')

args = parser.parse_args()

fname = args.name

f = h5py.File(fname, 'r')
remark = np.array(f['remark'])
if remark:
    print remark
fwhm = np.array(f['FWHM'])
print 'Saved FWHM = %.02f um' %(fwhm*1000)

raw = np.array(f['raw-scan'])
motor_position = raw[:,0] #first column
incident_I = raw[:,1] # 2nd column
knifeedge_I = raw[:,2] # 3rd column

normalized_I = np.divide(knifeedge_I, incident_I)
diff_I = np.gradient(normalized_I, motor_position) # take derivative
diff_I[np.isnan(diff_I)] = 0 # convert all NaNs (divZero) to 0

if normalized_I[:5].mean() > normalized_I[-5:].mean():
    diff_I = diff_I*-1

y = diff_I - np.max(diff_I)/2

if motor_position[0]>motor_position[1]:
    spline = scipy.interpolate.UnivariateSpline(motor_position[::-1], y[::-1], s=0)
else:
    spline = scipy.interpolate.UnivariateSpline(motor_position, y, s=0)
try:
    roots = spline.roots()
    if roots.size == 2:
        r1 = roots[0]
        r2 = roots[1]
    elif roots.size>2:
        rmax = np.argmax(abs(np.diff(roots)))
        r1 = roots[rmax]
        r2 = roots[rmax+1]
    else:
        r1 = 0
        r2 = 0
except Exception as e:
    print e
    r1 = 0
    r2 = 0


fwhm = abs(r2-r1)


plt.figure(1)
plt.subplot(211)
plt.plot(motor_position, normalized_I, 'bo')
plt.title('Knife-edge step scan')

plt.subplot(212)
plt.plot(motor_position, diff_I)

if fwhm>0:
    if r1<r2:
        plt.axvspan(r1, r2, facecolor='g', alpha=0.5)
    else:
        plt.axvspan(r2, r1, facecolor='g', alpha=0.5)
    plt.hlines(np.max(diff_I)/2, np.min(motor_position), np.max(motor_position))
    plt.title('FWHM = %.02f $\mu$m' %(fwhm*1000))
else:
    plt.title('FWHM not found')

plt.show()
