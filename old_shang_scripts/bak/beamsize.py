# -*- coding: utf-8 -*-
import os
import sys
import numpy as np

dir = '2015_1009_startup'
fname = os.path.join(dir, sys.argv[1])
#print fname

motor, I0, I1 = np.genfromtxt(fname, skip_header=16, unpack=True)
diffI = np.diff(I1.astype(float))

with open(fname + '.diff', 'w') as fout:
  for n1, n2 in zip(motor.astype(float), diffI):
    fout.write("%.03f, %.03f\n" %(n1, n2))
    
x = motor.astype(float)[:-1]
y = np.fabs(diffI) - np.max(np.fabs(diffI))/2
#print x.size, y.size
#print diffI, np.max(np.fabs(diffI))

import scipy.interpolate 
spline = scipy.interpolate.UnivariateSpline(x, y, s=0)
r1, r2 = spline.roots()
fwhm = np.fabs(r2-r1)
#print r1, r2, fwhm

import pylab as pl

pl.figure(1)
pl.subplot(211)
pl.plot(motor.astype(float), I1.astype(float), 'bo')
pl.title('Knife-edge step scan')

pl.subplot(212)
pl.plot(x, y)
pl.axvspan(r1, r2, facecolor='g', alpha=0.5)
pl.title('FWHM = %.03f mm' %fwhm)
pl.show()