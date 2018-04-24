# -*- coding: utf-8 -*-
import sys
import glob
import time
import numpy as np
import os

fileRootName = sys.argv[1]

datPath = '/home/biocat/SAXS_data/test/dat/'
datPath = os.path.join(datPath, fileRootName)
subtractPath = os.path.join(datPath, 'subtract/')

os.chdir(subtractPath)
RgFiles = sorted(glob.glob(fileRootName + '_????Rg.txt'))
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
    Rglist.append(0.0)
    RgError.append(0.0)
    I0list.append(0.0)
    I0Error.append(0.0)  


with open(fileRootName + '_Rg.csv', 'w') as fout:
  for n1, n2, n3, n4, n5 in zip(fileid, Rglist, RgError, I0list, I0Error):
    fout.write("%d, %.2f, %.2f, %.2f, %.2f\n" %(n1, n2, n3, n4, n5))

import subprocess
#open gnuplot
proc = subprocess.Popen(['gnuplot', '-p'], shell = True, stdin=subprocess.PIPE,)
gnuplotCmd = "plot '%s' u 1:2:3 w errorbars\n" % (fileRootName +'_Rg.csv')
print gnuplotCmd
proc.stdin.write(gnuplotCmd)

proc1 = subprocess.Popen(['gnuplot', '-p'], shell = True, stdin=subprocess.PIPE,)
gnuplotCmd = "plot '%s' u 1:4:5 w errorbars\n" % (fileRootName +'_Rg.csv')
print gnuplotCmd
proc1.stdin.write(gnuplotCmd)

time.sleep(1)
#quit gnuplot
proc.stdin.write('quit\n')
proc1.stdin.write('quit\n')

