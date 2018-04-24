# -*- coding: utf-8 -*-
import sys
import glob
import time
import numpy as np
import os

parameterFile = sys.argv[1]
samPrefix = sys.argv[2]
bufPrefix = sys.argv[3]

parameter = {}
execfile (parameterFile, parameter)

datPath = os.path.join(parameter["workPath"], 'dat/')
subtractPath = os.path.join(datPath, 'subtract/')
sambufPath = os.path.join(subtractPath, samPrefix + '-' + bufPrefix)

os.chdir(sambufPath)
#for timepoint in range(0, int(totalTimepoints)):
datFiles = sorted(glob.glob('%s-%s_?????.dat' %(samPrefix, bufPrefix)))
for sambufFile in datFiles:
  RgFile = sambufFile[:-4] + 'Rg.txt'
  autorgCmd = 'autorg %s -o %s -f ssv' %(sambufFile, RgFile)
  if not os.path.isfile(RgFile):
    os.system(autorgCmd)
    print autorgCmd

import subprocess
#open gnuplot
procRg = subprocess.Popen(['gnuplot', '-p'], shell = True, stdin=subprocess.PIPE,)
procI0 = subprocess.Popen(['gnuplot', '-p'], shell = True, stdin=subprocess.PIPE,)
procRg.stdin.write("cd '%s'\n" %sambufPath)
procI0.stdin.write("cd '%s'\n" %sambufPath)
procRg.stdin.write('set xrange [0:]\n')
procI0.stdin.write('set xrange [0:]\n')
procRg.stdin.write('set yrange [0:]\n')
procI0.stdin.write('set yrange [0:]\n')

prefix = '%s-%s' %(samPrefix, bufPrefix)
RgFiles = sorted(glob.glob(prefix + '_?????Rg.txt'))
fileid = []
Rglist = []
RgError = []
I0list = []
I0Error = []
for fname in RgFiles:
  fileid.append(int(fname[-10:-6]))

  if os.stat(fname).st_size > 0:
    f = open(fname, 'r')
    line = f.readline()
    columns = line.split()
    Rglist.append(float(columns[0]))
    RgError.append(float(columns[1]))
    I0list.append(float(columns[2]))
    I0Error.append(float(columns[3]))  
  else:
    Rglist.append(0.01)
    RgError.append(0.01)
    I0list.append(0.01)
    I0Error.append(0.01)

with open(prefix + '_Rg.csv', 'w') as fout:
  for n1, n2, n3, n4, n5 in zip(fileid, Rglist, RgError, I0list, I0Error):
      fout.write("%d, %.2f, %.2f, %.2f, %.2f\n" %(n1, n2, n3, n4, n5))

gnuplotCmd = "plot '%s' u 1:2:3 w errorbars t '%s'\n" % (prefix +'_Rg.csv', prefix + ' Rg')
#print gnuplotCmd
procRg.stdin.write(gnuplotCmd)
procRg.stdin.write('set terminal png\n')
procRg.stdin.write("set output '%s_Rg.png'\n" %prefix)
procRg.stdin.write(gnuplotCmd)
procRg.stdin.write('set terminal wxt\n')
  
gnuplotCmd = "plot '%s' u 1:4:5 w errorbars t '%s'\n" % (prefix +'_Rg.csv', prefix + ' I(0)')
#print gnuplotCmd
procI0.stdin.write(gnuplotCmd)
procI0.stdin.write('set terminal png\n')
procI0.stdin.write("set output '%s_I0.png'\n" %prefix)
procI0.stdin.write(gnuplotCmd)
procI0.stdin.write('set terminal wxt\n')

#quit gnuplot
time.sleep(60)
procRg.stdin.write('quit\n')
procI0.stdin.write('quit\n')

