# -*- coding: utf-8 -*-
import sys
import glob
import time
import numpy as np
import os

parameterFile = sys.argv[1]
subDir = sys.argv[2]
prefix = sys.argv[3]

parameter = {}
execfile (parameterFile, parameter)

datPath = os.path.join(parameter["workPath"], 'dat/' + subDir)
os.chdir(datPath)

processedDir = os.path.join(datPath, 'processed/')
if not os.path.exists(processedDir):
  os.system('mkdir ' + processedDir)

frameList = sys.argv[4:]

Frames = ''
for i in frameList:
  frameFileName = prefix + '_%04d.dat ' % int(i)
  Frames += frameFileName
averageCmd = 'dataver %s -o %s_avg.dat' %(Frames, os.path.join(processedDir, prefix))
print averageCmd +'\n'
os.system(averageCmd)

