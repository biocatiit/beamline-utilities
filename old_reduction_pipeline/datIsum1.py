# -*- coding: utf-8 -*-
import sys
import glob
import time
import numpy as np

code = sys.argv[1]

import matplotlib.pyplot as plt
plt.ion() # enable interactive plotting

while True:
  datfiles = sorted(glob.glob(code + '_*.dat'))
#with open('datfiles.txt', 'w') as f:
#  for dat in datfiles:
#    f.write("%s\n" %dat)

  sumlist = []
  for fname in datfiles:
    q, I, error = np.genfromtxt(fname, skip_header=2, skip_footer=18, unpack=True)
    sumlist.append(I.sum())
    plt.plot(sumlist,'o')
    plt.draw()
  time.sleep(10)
