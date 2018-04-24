# -*- coding: utf-8 -*-
import sys
import numpy as np
import h5py
import matplotlib.pyplot as plt
import scipy.interpolate

fname = sys.argv[1]

f = h5py.File(fname, 'r')
remark = np.array(f['remark'])
print remark
fwhm = np.array(f['FWHM'])
print 'FWHM = %.03f mm' %fwhm

raw = np.array(f['raw-scan'])
motor_position = raw[:,0] #first column
incident_I = raw[:,1] # 2nd column
knifeedge_I = raw[:,2] # 3rd column

normalized_I = np.divide(knifeedge_I, incident_I)
diff_I = np.diff(normalized_I) # take derivative
diff_I[np.isnan(diff_I)] = 0 # convert all NaNs (divZero) to 0

x = motor_position[:-1] #number of data points reduced by 1 after taking derivative
y = np.fabs(diff_I) - np.max(np.fabs(diff_I))/2

if x[0]>x[1]:
    spline = scipy.interpolate.UnivariateSpline(x[::-1], y[::-1], s=0)
else:
    spline = scipy.interpolate.UnivariateSpline(x, y, s=0)
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


fwhm = np.fabs(r2-r1)


plt.figure(1)
plt.subplot(211)
plt.plot(motor_position, normalized_I, 'bo')
plt.title('Knife-edge step scan')

plt.subplot(212)
plt.plot(x, abs(diff_I))

if fwhm>0:
    if r1<r2:
        plt.axvspan(r1, r2, facecolor='g', alpha=0.5)
    else:
        plt.axvspan(r2, r1, facecolor='g', alpha=0.5)
    plt.hlines(np.max(abs(diff_I))/2, np.min(x), np.max(x))
    plt.title('FWHM = %.02f $\mu$m' %(fwhm*1000))
else:
    plt.title('FWHM not found')

plt.show()
