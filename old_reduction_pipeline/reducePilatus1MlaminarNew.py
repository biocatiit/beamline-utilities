# -*- coding: utf-8 -*-
import time
import glob
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import Image
import subprocess

parameterFile = sys.argv[1]
fileRootName = sys.argv[2]

parameter = {}
execfile (parameterFile, parameter)

# USER SETTINGS START #
#### Set correct directories ####

tifPath = parameter["tifPath"]
headerPath = parameter["headerPath"]
workPath = parameter["workPath"]
# check dat dir
datPath = os.path.join(workPath, 'dat/')
if not os.path.exists(datPath):
  os.system('mkdir ' + datPath)
# check subdir 
datPath = os.path.join(datPath, fileRootName)
if not os.path.exists(datPath):
  os.system('mkdir ' + datPath)

#### Change beam center, fit2d mask file, qaxis file 
beamCenterX = parameter["beamCenterX"]
beamCenterY = parameter["beamCenterY"]
fit2dmask = os.path.join(workPath, parameter["fit2dmaskFile"])
qaxis = os.path.join(workPath, parameter["qaxisFile"])
# USER SETTINGS END #

#open gnuplot
proc = subprocess.Popen(['gnuplot', '-p'], shell = True, stdin=subprocess.PIPE,)
#proc.stdin.write('set log x\n')
proc.stdin.write('set log y\n')
proc.stdin.write('set xrange [0.004:0.4]\n')
proc.stdin.write("cd '%s'\n" %datPath)

oldtifname = 'old.dat'
oldoldtifname = 'oldold.dat'

plt.ion() #turn on interactive mode on plot
while True:
  newlist = sorted(glob.glob(tifPath + fileRootName + '_*.tif'))
  #print newlist
  for tif in newlist:
    path, tifname = os.path.split(tif)
    
    if not os.path.isfile(os.path.join(datPath, tifname[:-3] + 'dat')):
      os.chdir(datPath)
      radaverCommand = 'radaver -x %.2f -y %.2f --beamstop-mask=%s --axis-data=%s %s %s' %(beamCenterX, beamCenterY, fit2dmask, qaxis,  headerPath + tifname[:-9] + '.txt', tif)
      os.system(radaverCommand)
      print(radaverCommand)
      print tifname + ' ---> ' + tifname[:-3] + 'dat done;'
      # join 4 neighboring data points
      datregridCmd = 'datregrid --join=4 -o %s %s' %('r4'+tifname[:-3]+'dat', tifname[:-3]+'dat')
      gnuplotCmd = "plot '%s' u 1:2:3 w yerrorbars, '%s' u 1:2 w l, '%s' u 1:2 w l\n" % ('r4'+tifname[:-3]+'dat', oldtifname[:-3]+'dat', oldoldtifname[:-3]+'dat')
      print gnuplotCmd
      proc.stdin.write(gnuplotCmd)      
      oldoldtifname = oldtifname
      oldtifname = tifname
    print 'Press Ctrl+C to exit!'
    time.sleep(0.05)
  time.sleep(0.5)

#quit gnuplot
proc.stdin.write('quit\n')
