# -*- coding: utf-8 -*-
import sys
import glob
import time
import numpy as np
import os

parameterFile = sys.argv[1]
fileRootName = sys.argv[2]
bufferLow = int(sys.argv[3])
bufferHigh = int(sys.argv[4])
sampleLow = int(sys.argv[5])
sampleHigh = int(sys.argv[6])


parameter = {}
execfile (parameterFile, parameter)
datPath = os.path.join(parameter["workPath"], 'dat/' + fileRootName)
os.chdir(datPath)

bufferList = range(bufferLow, bufferHigh + 1)
sampleList = range(sampleLow, sampleHigh + 1)

#datPath = '/home/biocat/SAXS_data/Chen_2014_0305/dat/'
#datPath = os.path.join(datPath, fileRootName)
#os.chdir(datPath)

bufferFiles = ''
averagedBuffer = fileRootName + '_buf%d-%d.dat' % (bufferLow, bufferHigh)
for i in bufferList:
  bufferFileName = fileRootName + '_%04d.dat ' % i
  bufferFiles += bufferFileName
averageCmd = 'dataver %s -o %s' %(bufferFiles, averagedBuffer)
print averageCmd +'\n'
os.system(averageCmd)

sampleFiles = ''
averagedSample = fileRootName + '_sam%d-%d.dat' % (sampleLow, sampleHigh)
for i in sampleList:
  sampleFileName = fileRootName + '_%04d.dat ' % i
  sampleFiles += sampleFileName
averageCmd = 'dataver %s -o %s' %(sampleFiles, averagedSample)
print averageCmd +'\n'
os.system(averageCmd)

subtractedFile = '%s_%d-%d_%d-%d.dat' %(fileRootName, sampleLow, sampleHigh, bufferLow, bufferHigh)
subtractCmd = 'datop SUB %s %s -o %s' %(averagedSample, averagedBuffer, subtractedFile)
print subtractCmd
os.system(subtractCmd)

RgFile = '%s_%d-%d_%d-%dRg.txt' %(fileRootName, sampleLow, sampleHigh, bufferLow, bufferHigh)
autorgCmd = 'autorg %s -o %s -f ssv' %(subtractedFile, RgFile)
print autorgCmd
os.system(autorgCmd)

os.system('cat ' + RgFile)
