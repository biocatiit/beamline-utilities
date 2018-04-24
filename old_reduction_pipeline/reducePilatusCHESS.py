# -*- coding: utf-8 -*-
import time
import glob
import os
import numpy as np
import matplotlib.pyplot as plt
import sys

parameterFile = sys.argv[1]
print parameterFile
prefix = sys.argv[2]
print prefix
#cycle = int(sys.argv[3])
#print sys.argv[3]
#frame = int(sys.argv[3])


parameter = {}
execfile (parameterFile, parameter)

# USER SETTINGS START #
#### Set correct directories ####

tifPath = parameter["tifPath"]
logPath = parameter["logPath"]
workPath = parameter["workPath"]
# check dat dir
datPath = os.path.join(workPath, 'dat/')
if not os.path.exists(datPath):
  os.system('mkdir ' + datPath)
# check subdir 
datPath = os.path.join(datPath, prefix)
if not os.path.exists(datPath):
  os.system('mkdir ' + datPath)
# check header dir
headerPath = os.path.join(workPath, 'header/')
if not os.path.exists(headerPath): 
  os.system('mkdir ' + headerPath)


#### Change beam center, fit2d mask file, qaxis file 
beamCenterX = parameter["beamCenterX"]
beamCenterY = parameter["beamCenterY"]
fit2dmask = os.path.join(workPath, parameter["fit2dmaskFile"])
qaxis = os.path.join(workPath, parameter["qaxisFile"])
# USER SETTINGS END #

print "Beam Center on detector (Pixel XY): %02f, %02f" %(beamCenterX, beamCenterY)
# Convert entry lines in the log file to the header file for each Pilatus tif file
#logFile = os.path.join(logPath, prefix + '.log')
#print logFile
#with open(logFile, 'r') as f:
  #title = f.readline() # ignore the 1st title line
  #cycle = 1
  #for line in f:
    #columns = line.split()
    #incident = columns[1]
    #transmitted = columns[2]
    #incident = columns[3]
    #exposure = columns[4]
    #for i in range(0, frame):
      #headerFile = os.path.join(headerPath, '%s%04d_%05d' %(prefix, cycle, i))
      #fout = open(headerFile, 'w')
      #fout.writelines('Exposure time [s]: %s\n' %exposure)
      #fout.writelines('Transmitted Beam: %s\n' %transmitted)
      #fout.writelines('Incident Beam: %s\n' %incident)
      #fout.writelines('Code: %s\n' %prefix)
      #fout.writelines('Concentration [mg/ml]: 1')
      #fout.writelines('Run number: %d' %i)
      #fout.close()
    #cycle += 1
#print "========header generated========"
print "---No header file used---Raw curve UNSCALED!!!"

os.chdir(datPath)
print datPath
filePattern = tifPath + prefix + '_*.tif' 
print filePattern
newlist = sorted(glob.glob(filePattern))
for tif in newlist:
  path, tifname = os.path.split(tif)
  if not os.path.isfile(os.path.join(datPath, tifname[:-3] + 'dat')):
    radaverCommand = 'radaver -x %.2f -y %.2f --beamstop-mask=%s --axis-data=%s %s' %(beamCenterX, beamCenterY, fit2dmask, qaxis, tif)
    os.system(radaverCommand)
    #print(radaverCommand)
    print tifname + ' ---> ' + tifname[:-3] + 'dat done!'
  
