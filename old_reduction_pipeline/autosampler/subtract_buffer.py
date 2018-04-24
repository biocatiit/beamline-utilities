# -*- coding: utf-8 -*-
import sys
import glob
import time
import numpy as np
import os

parameterFile = sys.argv[1]
subDir = sys.argv[2]
samplePrefix = sys.argv[3]
bufferPrefix = sys.argv[4]

parameter = {}
execfile (parameterFile, parameter)

datPath = os.path.join(parameter["workPath"], 'dat/' + subDir)
processedDir = os.path.join(datPath, 'processed/')
os.chdir(processedDir)
print processedDir

subtractCmd = 'datop SUB %s_avg.dat %s_avg.dat -o %s.dat' %(samplePrefix, bufferPrefix, samplePrefix)
print subtractCmd +'\n'
os.system(subtractCmd)

RgFile = '%s_Rg.txt' %(samplePrefix)
autorgCmd = 'autorg %s.dat -o %s -f ssv' %(samplePrefix, RgFile)
print autorgCmd
os.system(autorgCmd)

os.system('cat ' + RgFile)

