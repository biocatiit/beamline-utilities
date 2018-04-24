# -*- coding: utf-8 -*-
import sys
import time
import glob
import os
import numpy as np
import Image
import subprocess
import matplotlib.pyplot as plt
plt.ion() # enable interactive plotting

tifPath = '/mnt/detectors/Pilatus100/Osman_2014_0210/'
#tifPath = '/home/biocat/SAXS_data/Osman_20140208/water/'
workPath = '/home/biocat/SAXS_data/Osman_20140208/'
datPath = os.path.join(workPath, 'frame/')
#headerPath = os.path.join(workPath, 'header/') # use tif only, no header file/transmitted intensity
fileRootName = sys.argv[1]

beamCenterX = 22.75
beamCenterY = 176.49
fit2dmask = os.path.join(workPath, 'fit2d20140208.msk')
qaxis = os.path.join(workPath, 'qaxis20140208.dat')

#open gnuplot
proc = subprocess.Popen(['gnuplot', '-p'], shell = True, stdin=subprocess.PIPE,)
proc.stdin.write('set log y\n')
#proc.stdin.write('set yrange [1:100]\n')
proc.stdin.write("cd '%s'\n" %datPath)

def log_transform(im):
    '''returns log(image) scaled to the interval [0,1]'''
    try:
        (min, max) = (im[im > 0].min(), im.max())
        if (max > min) and (max > 0):
            return (np.log(im.clip(min, max)) - np.log(min)) / (np.log(max) - np.log(min))
    except:
        pass
    return im

oldtifname = 'old.dat'
oldoldtifname = 'oldold.dat'

newlist = sorted(glob.glob(tifPath + fileRootName +'*.tif'))
for tif in newlist:
  print tif
  path, tifname = os.path.split(tif)
  if not os.path.isfile(os.path.join(datPath, tifname[:-3] + 'dat')):
    im = Image.open(tif)
    img = np.array(im)
    plt.imshow(log_transform(img))
    plt.draw()

    os.chdir(datPath)
    radaverCommand = 'radaver -x %.2f -y %.2f --beamstop-mask=%s --axis-data=%s %s' %(beamCenterX, beamCenterY, fit2dmask, qaxis, tif)
    print radaverCommand
    #radaverCommand = 'radaver -x %.2f -y %.2f --axis-data=%s %s' %(beamCenterX, beamCenterY, qaxis, tif)
    os.system(radaverCommand)
    print tifname + ' ---> ' + tifname[:-3] + 'dat done!'
    gnuplotCmd = "plot '%s' u 1:2:3 w yerrorbars, '%s' u 1:2 w l, '%s' u 1:2 w l\n" % (tifname[:-3]+'dat', oldtifname[:-3]+'dat', oldoldtifname[:-3]+'dat')
    print gnuplotCmd
    proc.stdin.write(gnuplotCmd)
    oldoldtifname = oldtifname
    oldtifname = tifname
    
    time.sleep(5)

#quit gnuplot
proc.stdin.write('quit\n')
