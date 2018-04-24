# -*- coding: utf-8 -*-
import sys
import glob
import time
import numpy as np
import os

parameterFile = sys.argv[1]
subDir = sys.argv[2]

parameter = {}
execfile (parameterFile, parameter)

#datPath = '/home/biocat/SAXS_data/Woodson_2014_0226/dat/'
datPath = os.path.join(parameter["workPath"], 'dat/' + subDir)
os.chdir(datPath)

import subprocess
proc = subprocess.Popen(['gnuplot', '-p'], shell = True, stdin=subprocess.PIPE,)
proc.stdin.write("cd '%s'\n" %datPath)
proc.stdin.write('set xrange [0:]\n')
proc.stdin.write('set yrange [3.5E3:5E3]\n')

while True:
  datfiles = sorted(glob.glob('*_????.dat'), key=os.path.getctime)
  print datfiles[-4:]
  fileid = []
  i = 1
  sumlist = []
  for fname in datfiles:
    fileid.append(i)
    try:
      q, I, error = np.genfromtxt(fname, skip_header=2, skip_footer=18, unpack=True)
      sumlist.append(I.sum())
    except:
      sumlist.append(0)
    i+=1 
  with open(subDir + '.csv', 'w') as fout:
    for n1, n2 in zip(fileid, sumlist):
      fout.write("%d, %.1f\n" %(n1, n2))
  print 'Update and plot the integrated intensity in ' + subDir + '.csv'
  gnuplotCmd = "plot '%s' u 1:2 w boxes\n" % (subDir +'.csv')
  proc.stdin.write(gnuplotCmd)
  print 'Press Ctrl+C to exit!'
  proc.stdin.write('set terminal png\n')
  proc.stdin.write("set output '%s_sum.png'\n" %subDir)
  proc.stdin.write(gnuplotCmd)
  proc.stdin.write('set terminal wxt\n')
  time.sleep(3)

#quit gnuplot
proc.stdin.write('quit\n')
