# -*- coding: utf-8 -*-
import sys
import glob
import time
import numpy as np
import os

parameterFile = sys.argv[1]
samPrefix = sys.argv[2]
samShots = sys.argv[3]
samTimepoints = sys.argv[4]
bufPrefix = sys.argv[5]
bufShots = sys.argv[6]
bufTimepoints = sys.argv[7]

reduceSampleCmd = 'python sf_reducePilatus.py %s %s %s' %(parameterFile, samPrefix, samTimepoints)
os.system(reduceSampleCmd)
print reduceSampleCmd

averageSampleCmd = 'python sf_sort_timepoint.py %s %s %s %s' %(parameterFile, samPrefix, samShots, samTimepoints)
os.system(averageSampleCmd)
print averageSampleCmd

reduceBufferCmd = 'python sf_reducePilatus.py %s %s %s' %(parameterFile, bufPrefix, bufTimepoints)
os.system(reduceBufferCmd)
print reduceBufferCmd

averageBufferCmd = 'python sf_sort_timepoint.py %s %s %s %s' %(parameterFile, bufPrefix, bufShots, bufTimepoints)
os.system(averageBufferCmd)
print averageBufferCmd

subtractionCmd = 'python sf_buffer_subtraction.py %s %s %s %s %s' %(parameterFile, samPrefix, bufPrefix, samShots, samTimepoints)
os.system(subtractionCmd)
print subtractionCmd

autoguinierCmd = 'python sf_autoguinier.py %s %s %s' %(parameterFile, samPrefix, bufPrefix)
os.system(autoguinierCmd)
print autoguinierCmd

