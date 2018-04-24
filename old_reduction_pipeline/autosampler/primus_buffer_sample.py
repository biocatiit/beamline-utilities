# -*- coding: utf-8 -*-
import sys
import glob
import time
import numpy as np
import os

parameterFile = sys.argv[1]
subDir = sys.argv[2]
bufferPrefix = sys.argv[3]
bufferLow = int(sys.argv[4])
bufferHigh = int(sys.argv[5])
samplePrefix = sys.argv[6]
sampleLow = int(sys.argv[7])
sampleHigh = int(sys.argv[8])


parameter = {}
execfile (parameterFile, parameter)

datPath = os.path.join(parameter["workPath"], 'dat/' + subDir)
os.chdir(datPath)


bufferList = range(bufferLow, bufferHigh + 1)

bufferFrames = ''
for i in bufferList:
  frameFileName = bufferPrefix + '_%04d.dat ' % i
  bufferFrames += frameFileName

sampleList = range(bufferLow, bufferHigh + 1)
sampleFrames = ''
for i in sampleList:
  frameFileName = samplePrefix + '_%04d.dat ' % i
  sampleFrames += frameFileName

cmd = 'primus %s %s &' %(sampleFrames, bufferFrames)
print cmd +'\n'
os.system(cmd)

