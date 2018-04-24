# -*- coding: utf-8 -*-
import time
import glob
import os
import numpy as np
import matplotlib.pyplot as plt

tifPath = '/mnt/detectors/Pilatus100/Osman_2014_0208/'
workPath = '/home/biocat/SAXS_data/Osman_20140208/'
datPath = os.path.join(workPath, 'frame/')
headerPath = os.path.join(workPath, 'header/')

beamCenterX = 22.75
beamCenterY = 176.49
fit2dmask = os.path.join(workPath, 'fit2d20140208.msk')
qaxis = os.path.join(workPath, 'qaxis20140208.dat')

newlist = sorted(glob.glob(tifPath + '*.tif'))
for tif in newlist:
  path, tifname = os.path.split(tif)
    
  if not os.path.isfile(os.path.join(datPath, tifname[:-3] + 'dat')):
    os.chdir(datPath)
    if os.path.isfile(os.path.join(headerPath,  tifname[:-3] + 'txt')):
      radaverCommand = 'radaver -x %.2f -y %.2f --beamstop-mask=%s --axis-data=%s %s %s' %(beamCenterX, beamCenterY, fit2dmask, qaxis, os.path.join(headerPath,  tifname[:-3] + 'txt'), tif)
      os.system(radaverCommand)
      print tifname + ' ---> ' + tifname[:-3] + 'dat done!'
  
