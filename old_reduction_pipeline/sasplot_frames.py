# -*- coding: utf-8 -*-
import sys
import glob
import time
import numpy as np
import os

parameterFile = sys.argv[1]
fileRootName = sys.argv[2]
frameLow = int(sys.argv[3])
frameHigh = int(sys.argv[4])

parameter = {}
execfile (parameterFile, parameter)

#datPath = '/home/biocat/SAXS_data/Woodson_2014_0226/dat/'
datPath = os.path.join(parameter["workPath"], 'dat/' + fileRootName)
os.chdir(datPath)

frameList = range(frameLow, frameHigh + 1)

Frames = ''
for i in frameList:
  frameFileName = fileRootName + '_%04d.dat ' % i
  Frames += frameFileName
averageCmd = 'sasplot %s' %(Frames)
print averageCmd +'\n'
os.system(averageCmd)

