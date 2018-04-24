# -*- coding: utf-8 -*-
import sys
import glob
import time
import numpy as np
import os

parameterFile = sys.argv[1]
subDir = sys.argv[2]
prefix = sys.argv[3]
frameLow = int(sys.argv[4])
frameHigh = int(sys.argv[5])

parameter = {}
execfile (parameterFile, parameter)

datPath = os.path.join(parameter["workPath"], 'dat/' + subDir)
os.chdir(datPath)

frameList = range(frameLow, frameHigh + 1)

Frames = ''
for i in frameList:
  frameFileName = prefix + '_%04d.dat ' % i
  Frames += frameFileName
averageCmd = 'primus %s&' %(Frames)
print averageCmd +'\n'
os.system(averageCmd)

