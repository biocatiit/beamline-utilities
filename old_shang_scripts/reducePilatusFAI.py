# -*- coding: utf-8 -*-
import time
import glob
import os
import sys
import thread

print 'Usage: python image2data.py parameterFile fileRootName'

parameterFile = sys.argv[1]
fileRootName = sys.argv[2]

parameter = {}
execfile (parameterFile, parameter)

################################ USER SETTINGS START #
nPoints = int(parameter["NumberOfDataPoints"])
fMask = parameter["beamstopMaskEDF"]
fPONI = parameter["PONIfile"]
tifPath = parameter["tifPath"]
workPath = parameter["workPath"]
################################ USER SETTINGS END #

#### Setup correct directories ####
# check dat dir
datPath = os.path.join(workPath, 'dat/')
if not os.path.exists(datPath):
  os.system('mkdir ' + datPath)
# check subdir 
subdatPath = os.path.join(datPath, fileRootName)
if not os.path.exists(subdatPath):
  os.system('mkdir ' + subdatPath)

print datPath
debugfile = os.path.join(datPath, fileRootName + '.debug')
print debugfile
####################################################

####################################################
import pyFAI
import fabio

ai= pyFAI.load(fPONI)
ai.maskfile = fMask

####### Infinite loop to wait and convert detector images ########
while True:
  print 'Waiting for new detector images ...'
  time.sleep(3)
  fDebug = open(debugfile, 'w')
  newlist = sorted(glob.glob(tifPath + fileRootName + '_*.tif'))
  for tif in newlist:
    path, tifname = os.path.split(tif)
    outdat = tifname[:-3] + 'dat'
    if not os.path.isfile(os.path.join(datPath, outdat)):
      os.chdir(subdatPath)
      pilatusimg = fabio.open(tif)
      ai.integrate1d(data=pilatusimg.data, npt=nPoints,\
        unit='q_A^-1', error_model='poisson', filename=outdat)
      message = tifname + ' -> ' + outdat
      print message
      fDebug.write(message + '\n')
  fDebug.close()
