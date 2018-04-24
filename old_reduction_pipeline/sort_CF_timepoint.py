# -*- coding: utf-8 -*-
import sys
import glob
import time
import numpy as np
import os

parameterFile = sys.argv[1]
prefix = sys.argv[2]
parameter = {}
execfile (parameterFile, parameter)
samplePath = os.path.join(parameter["workPath"], 'dat/' + prefix)
os.chdir(samplePath)

totalShots = int(sys.argv[3]) # cycle
totalTimepoints = int(sys.argv[4]) # frame

print samplePath, totalShots, totalTimepoints

for timepoint in range(1, totalTimepoints + 1):
  Frames = ''
  TpointPath = os.path.join(samplePath, 't%04d' %timepoint)
  if not os.path.exists(TpointPath): os.mkdir(TpointPath)
  for shot in range(1, totalShots + 1):
    frameFileName = '%s_%04d_%04d.dat ' %(prefix, shot, timepoint)
    Frames += frameFileName
  os.system('cp %s %s' %(Frames, TpointPath))
  #print 'cp %s %s' %(Frames, TpointPath)
  averagedFrame = '%s_avg%04d.dat' %(prefix, timepoint)
  averageCmd = 'dataver %s -o %s' %(Frames, os.path.join(TpointPath,averagedFrame))
  #print averageCmd
  os.system(averageCmd)
  print 'Time point %04d copied and averaged!' %timepoint
    


