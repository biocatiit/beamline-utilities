# -*- coding: utf-8 -*-
import os
import sys
import numpy as np

fname = sys.argv[1]

# MX monochromator energy scan
energy, I0, I1 = np.genfromtxt(fname, skip_header=5, unpack=True)
diffI = np.diff(I1.astype(float))

# normalize against I0
normalized_I = np.divide(I1, I0)
# take derivative of the normalized intensity
diff_I = np.diff(normalized_I)

xx = energy[:-1]
yy = diff_I

from numpy import pi, exp
def Gaussian(x, A, mean, sigma):
    return A*exp(-(x-mean)**2/(2.0*sigma**2))
# FWHM = 2*sqrt(2*ln2)*sigma ~ 2.3548*sigma

init_vals = [-0.1, 12, 0.001]
from scipy.optimize import curve_fit
best_vals, covar = curve_fit(Gaussian, xx, yy, p0=init_vals)
print best_vals

import pylab as pl
pl.figure(1)
pl.subplot(211)
pl.plot(energy, normalized_I, 'o')
pl.title('Monochromator energy scan I1/I0')

pl.subplot(212)
pl.plot(xx, yy, 'o')
pl.plot(xx, Gaussian(xx, best_vals[0], best_vals[1], best_vals[2]))
pl.title('Gaussian center = %.03f +- %.03f keV' %(best_vals[1], best_vals[2]*1.1774))
pl.show() 
