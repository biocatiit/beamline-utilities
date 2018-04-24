# -*- coding: utf-8 -*-
import sys
import glob
import time
import numpy as np
import os

workPath= sys.argv[1]
fileRootName = sys.argv[2]
frameLow = int(sys.argv[3])
frameHigh = int(sys.argv[4])

os.chdir(workPath)

frameList = range(frameLow, frameHigh + 1)

Frames = ''
averagedFrame = fileRootName + '_%d-%d.dat' % (frameLow, frameHigh)
for i in frameList:
  frameFileName = fileRootName + '_%04d.dat ' % i
  Frames += frameFileName
averageCmd = 'dataver %s -o %s' %(Frames, averagedFrame)
print averageCmd +'\n'
os.system(averageCmd)

