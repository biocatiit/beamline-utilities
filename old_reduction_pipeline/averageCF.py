# -*- coding: utf-8 -*-
import time
import glob
import os
import numpy as np
import matplotlib.pyplot as plt

tifPath = '/mnt/detectors/Pilatus100/2013_1207Bilsel/'
workPath = '/home/weifeng/SAXS-data/20131208Bilsel/'
datPath = os.path.join(workPath, 'frame/')
headerPath = os.path.join(workPath, 'header/')

beamCenterX = 186.4
beamCenterY = 134.8
fit2dmask = os.path.join(workPath, 'fit2d20131208.msk')
qaxis = os.path.join(workPath, 'qaxis20131208.dat')

newlist = sorted(glob.glob(tifPath + 'FlowRateTest00??_?????.tif'))
for tif in newlist:
  path, tifname = os.path.split(tif)
    
  if not os.path.isfile(os.path.join(datPath, tifname[:-3] + 'dat')):
    if os.path.isfile(os.path.join(headerPath,  tifname[:-3] + 'txt')):
      #os.chdir(datPath)
      radaverCommand = 'radaver -x %.2f -y %.2f --beamstop-mask=%s --axis-data=%s --frame-directory=%s %s %s' %(beamCenterX, beamCenterY, fit2dmask, qaxis, datPath, headerPath + tifname[:-3] + 'txt', tif)
      os.system(radaverCommand)
      #print(radaverCommand)
      print tifname + ' ---> ' + tifname[:-3] + 'dat done!'
  
