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

frameList = sys.argv[4:]

Frames = ''
for i in frameList:
  frameFileName = prefix + '_%04d.dat ' % int(i)
  Frames += frameFileName
averageCmd = 'primus %s&' %(Frames)
print averageCmd +'\n'
os.system(averageCmd)

