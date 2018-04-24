# -*- coding: utf-8 -*-
import sys
import glob
import time
import numpy as np
import os

parameterFile = sys.argv[1]
fileRootName = sys.argv[2]

parameter = {}
execfile (parameterFile, parameter)
#datPath = os.path.join(parameter["workPath"], 'dat/' + fileRootName)
datPath = '/home/biocat/Shang/SWAXS/20140310/lyza/'
os.chdir(datPath)

frameLow = int(sys.argv[3])
frameHigh = int(sys.argv[4])

frameList = range(frameLow, frameHigh + 1)

Frames = ''
averagedFrame = fileRootName + '_%d-%d.dat' % (frameLow, frameHigh)
for i in frameList:
  frameFileName = fileRootName + '_%05d.dat ' % i
  Frames += frameFileName
averageCmd = 'dataver %s -o %s' %(Frames, averagedFrame)
print averageCmd +'\n'
os.system(averageCmd)
