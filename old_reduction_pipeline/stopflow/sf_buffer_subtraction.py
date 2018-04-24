# -*- coding: utf-8 -*-
import sys
import glob
import time
import numpy as np
import os

parameterFile = sys.argv[1]
samPrefix = sys.argv[2]
bufPrefix = sys.argv[3]
totalShots = int(sys.argv[4]) # cycle
totalTimepoints = int(sys.argv[5]) # frame

parameter = {}
execfile (parameterFile, parameter)

datPath = os.path.join(parameter["workPath"], 'dat/')
samPath = os.path.join(datPath, samPrefix)
bufPath = os.path.join(datPath, bufPrefix)
subtractPath = os.path.join(datPath, 'subtract/')
if not os.path.exists(subtractPath): os.mkdir(subtractPath)
sambufPath = os.path.join(subtractPath, samPrefix + '-' + bufPrefix)
if not os.path.exists(sambufPath): os.mkdir(sambufPath)

os.chdir(datPath)

for timepoint in range(0, totalTimepoints):
  samFile = os.path.join(samPath, 't%05d/%s_avg%05d.dat' %(timepoint, samPrefix, timepoint))
  bufFile = os.path.join(bufPath, 't%05d/%s_avg%05d.dat' %(timepoint, bufPrefix, timepoint))
  sambufFile = os.path.join(sambufPath, '%s-%s_%05d.dat' %(samPrefix, bufPrefix, timepoint))
  cmd = 'datop SUB %s %s -o %s' %(samFile, bufFile, sambufFile)
  os.system(cmd)
  print cmd
