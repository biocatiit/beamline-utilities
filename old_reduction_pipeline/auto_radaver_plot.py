# -*- coding: utf-8 -*-
import time
import glob
import os
import numpy as np
import subprocess

tifPath = '/mnt/detectors/Pilatus100/Osman_2014_0210/'
#tifPath = '/home/biocat/SAXS_data/Osman_20140208/water/'
workPath = '/home/biocat/SAXS_data/Osman_20140208/'
datPath = os.path.join(workPath, 'frame/')
#headerPath = os.path.join(workPath, 'header/') # use tif only, no header file/transmitted intensity

beamCenterX = 22.75
beamCenterY = 176.49
fit2dmask = os.path.join(workPath, 'fit2d20140208.msk')
qaxis = os.path.join(workPath, 'qaxis20140208.dat')

#open gnuplot
proc = subprocess.Popen(['gnuplot', '-p'], shell = True, stdin=subprocess.PIPE,)
proc.stdin.write('set log y\n')
proc.stdin.write('set yrange [1:100]\n')
proc.stdin.write("cd '%s'\n" %datPath)

newlist = sorted(glob.glob(tifPath + 'cheya*.tif'))
for tif in newlist:
  path, tifname = os.path.split(tif)
    
  if not os.path.isfile(os.path.join(datPath, tifname[:-3] + 'dat')):
    os.chdir(datPath)
    radaverCommand = 'radaver -x %.2f -y %.2f --beamstop-mask=%s --axis-data=%s %s' %(beamCenterX, beamCenterY, fit2dmask, qaxis, tif)
    print radaverCommand
    #radaverCommand = 'radaver -x %.2f -y %.2f --axis-data=%s %s' %(beamCenterX, beamCenterY, qaxis, tif)
    os.system(radaverCommand)
    print tifname + ' ---> ' + tifname[:-3] + 'dat done!'
    gnuplotCmd = "plot '%s' u 1:2 w l\n" % (tifname[:-3]+'dat')
    print gnuplotCmd
    proc.stdin.write(gnuplotCmd)
    time.sleep(1)

#quit gnuplot
proc.stdin.write('quit\n')
  
