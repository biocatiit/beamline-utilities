# -*- coding: utf-8 -*-
import sys
import glob
import time
import numpy as np
import os

parameterFile = sys.argv[1]
fileRootName = sys.argv[2]
Ymin = sys.argv[3]
Ymax = sys.argv[4]

parameter = {}
execfile (parameterFile, parameter)

datPath = os.path.join(parameter["workPath"], 'dat/' + fileRootName)
os.chdir(datPath)

import subprocess
proc = subprocess.Popen(['gnuplot', '-p'], shell = True, stdin=subprocess.PIPE,)
proc.stdin.write("cd '%s'\n" %datPath)
proc.stdin.write('set xrange [1:]\n')
proc.stdin.write('set yrange [%s:%s]\n' %(Ymin, Ymax))

while True:
  datfiles = sorted(glob.glob(fileRootName + '_????.dat'))
  fileid = []
  sumlist = []
  for fname in datfiles:
    fileid.append(int(fname[-8:-4]))
    try:
      q, I, error = np.genfromtxt(fname, skip_header=2, skip_footer=18, unpack=True)
      sumlist.append(I.sum())
    except:
      sumlist.append(0) 
  with open(fileRootName + '.csv', 'w') as fout:
    for n1, n2 in zip(fileid, sumlist):
      fout.write("%d, %.1f\n" %(n1, n2))
  print 'Update and plot the integrated intensity in ' + fileRootName + '.csv'
  gnuplotCmd = "plot '%s' u 1:2 w boxes\n" % (fileRootName +'.csv')
  proc.stdin.write(gnuplotCmd)
  print 'Press Ctrl+C to exit!'
  proc.stdin.write('set terminal png\n')
  proc.stdin.write("set output '%s_sum.png'\n" %fileRootName)
  proc.stdin.write(gnuplotCmd)
  proc.stdin.write('set terminal wxt\n')
  print gnuplotCmd
  time.sleep(0.2)

#quit gnuplot
proc.stdin.write('quit\n')
