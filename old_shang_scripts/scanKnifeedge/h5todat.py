# -*- coding: utf-8 -*-
import os
import sys
import numpy as np

fname = sys.argv[1]

import h5py
f = h5py.File(fname, 'r')
remark = np.array(f['remark'])
print remark
fwhm = np.array(f['FWHM'])
print 'FWHM = %.03f mm' %fwhm

raw = np.array(f['raw-scan'])
motor = raw[:,0] #first column
incident_I = raw[:,1] # 2nd column
knifeedge_I = raw[:,2] # 3rd column

normalized_I = np.divide(knifeedge_I, incident_I)
diff_I = np.diff(normalized_I) # take derivative
diff_I[np.isnan(diff_I)] = 0 # convert all NaNs (divZero) to 0


import pylab as pl

pl.figure(1)
pl.subplot(211)
pl.plot(motor, normalized_I, 'bo')
pl.title('Knife-edge step scan')


x = motor[:-1]
y = np.fabs(diff_I)

pl.subplot(212)
pl.plot(x, y)
pl.hlines(np.max(y)/2, np.min(x), np.max(x), label='Half Maximum')
pl.title('FWHM = %.03f mm' %fwhm)
pl.show()

derivative = np.array(zip(x,y))
np.savetxt(fname[:-3] + '.dat', derivative, delimiter = ' ', newline='\n')
print "np save text " + fname[:-3] + '.dat'
