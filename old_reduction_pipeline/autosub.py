# -*- coding: utf-8 -*-
import sys
import glob
import time
import numpy as np
import os

parameterFile = sys.argv[1]
fileRootName = sys.argv[2]
#bufferFileNumber = int(sys.argv[3])
#bufferName = '%s_%04d.dat' %(fileRootName, bufferFileNumber)
bufferName = sys.argv[3]

parameter = {}
execfile (parameterFile, parameter)

datPath = os.path.join(parameter["workPath"], 'dat/' + fileRootName)
subtractPath = os.path.join(datPath, 'subtract/')
if not os.path.exists(subtractPath):
  os.system('mkdir ' + subtractPath)

import subprocess
#open gnuplot
procRg = subprocess.Popen(['gnuplot', '-p'], shell = True, stdin=subprocess.PIPE,)
procI0 = subprocess.Popen(['gnuplot', '-p'], shell = True, stdin=subprocess.PIPE,)
procRg.stdin.write("cd '%s'\n" %subtractPath)
procI0.stdin.write("cd '%s'\n" %subtractPath)
procRg.stdin.write('set xrange [0:]\n')
procI0.stdin.write('set xrange [0:]\n')
procRg.stdin.write('set yrange [0:200]\n')
procI0.stdin.write('set yrange [0:5]\n')


while True:
  os.chdir(datPath)
  datfiles = sorted(glob.glob(fileRootName + '_????.dat'))
  for fname in datfiles:
    subtractFileName = fname[:-4]+'sub.dat'
    if not os.path.isfile(os.path.join(subtractPath, subtractFileName)):
      subtractCmd = 'datop SUB %s %s -o subtract/%s' %(fname, bufferName, subtractFileName)
      print subtractCmd
      os.system(subtractCmd)
      time.sleep(0.1) # give datop some time to complete!
  
    RgFileName = fname[:-4]+'Rg.txt'
    if not os.path.isfile(os.path.join(subtractPath, RgFileName)):
      autorgCmd = 'autorg subtract/%s -o subtract/%s -f ssv' %(subtractFileName, RgFileName)
      print autorgCmd
      os.system(autorgCmd)
      time.sleep(0.1) # give autorg some time to complete!

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
      Rglist.append(0.01)
      RgError.append(0.01)
      I0list.append(0.01)
      I0Error.append(0.01)

  with open(fileRootName + '_Rg.csv', 'w') as fout:
    for n1, n2, n3, n4, n5 in zip(fileid, Rglist, RgError, I0list, I0Error):
      fout.write("%d, %.2f, %.2f, %.2f, %.2f\n" %(n1, n2, n3, n4, n5))

  gnuplotCmd = "plot '%s' u 1:2:3 w errorbars\n" % (fileRootName +'_Rg.csv')
  #print gnuplotCmd
  procRg.stdin.write(gnuplotCmd)
  procRg.stdin.write('set terminal png\n')
  procRg.stdin.write("set output '%s_Rg.png'\n" %fileRootName)
  procRg.stdin.write(gnuplotCmd)
  procRg.stdin.write('set terminal wxt\n')
  time.sleep(1)
  
  gnuplotCmd = "plot '%s' u 1:4:5 w errorbars\n" % (fileRootName +'_Rg.csv')
  #print gnuplotCmd
  procI0.stdin.write(gnuplotCmd)
  procI0.stdin.write('set terminal png\n')
  procI0.stdin.write("set output '%s_I0.png'\n" %fileRootName)
  procI0.stdin.write(gnuplotCmd)
  procI0.stdin.write('set terminal wxt\n')
  time.sleep(0.1)
  print 'Press Ctrl+C to exit!'
  time.sleep(0.2)

#quit gnuplot
procRg.stdin.write('quit\n')
procI0.stdin.write('quit\n')

