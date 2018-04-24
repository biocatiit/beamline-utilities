# -*- coding: utf-8 -*-
import time
import glob
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import subprocess

parameterFile = sys.argv[1]
fileRootName = sys.argv[2]
logFile = sys.argv[3]

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
datPath = os.path.join(datPath, fileRootName)
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


def convertLog2Header(logfile, tifname):
  print logfile
  os.chdir(headerPath)
  with open(os.path.join(logPath, logfile), 'r') as f:
    title = f.readline() # ignore the 1st title line
    for line in f:
      columns = line.split()
      #wrong naming scheme, does not worth my effort! 20140413
      #fnameinlog = columns[0]
      #headername = fnameinlog[:-5] + fnameinlog[-4:] + '_05d'%
      incident = columns[1]
      transmitted = columns[2]
      I1overI0 = columns[3]
      exposure = columns[4]
        
      fout = open(tifname[:-4] + '.txt', 'w')
      fout.writelines('Exposure time [s]: %s\n' %exposure)
      fout.writelines('Transmitted Beam: %s\n' %transmitted)
      fout.writelines('Incident Beam: %s\n' %incident)
      fout.writelines('Code: %s\n' %tifname[:-4])
      fout.writelines('Concentration [mg/ml]: 1\n')
      #fout.writelines('Run Number: %s\n' %headername[-4:])
      fout.close
      #print 'Header file: ' + headername + '.txt created!'

#open gnuplot
proc = subprocess.Popen(['gnuplot', '-p'], shell = True, stdin=subprocess.PIPE,)
proc.stdin.write('set log x\n')
proc.stdin.write('set log y\n')
proc.stdin.write('set xrange [0.004:0.4]\n')
proc.stdin.write("cd '%s'\n" %datPath)

oldtifname = 'old.dat'
oldoldtifname = 'oldold.dat'

newlist = sorted(glob.glob(tifPath + fileRootName + '_?????.tif'))
for tif in newlist:
  path, tifname = os.path.split(tif)
    
  if not os.path.isfile(os.path.join(datPath, tifname[:-3] + 'dat')):
    if not os.path.isfile(os.path.join(headerPath,  tifname[:-3] + 'txt')):
      convertLog2Header(logFile, tifname)
    if os.path.isfile(os.path.join(headerPath,  tifname[:-3] + 'txt')):
	# make sure header file exist. e.g. the last frame, tif exists but not in log
	os.chdir(datPath)
	radaverCommand = 'radaver --beam-center-x=%.2f --beam-center-y=%.2f --axis-data=%s %s %s' %(beamCenterX, beamCenterY, qaxis,  headerPath + tifname[:-3] + 'txt', tif)
	os.system(radaverCommand)
	time.sleep(1)
	print(radaverCommand)
	print tifname + ' ---> ' + tifname[:-3] + 'dat done;'
	gnuplotCmd = "plot '%s' u 1:2:3 w yerrorbars, '%s' u 1:2 w l, '%s' u 1:2 w l\n" % (tifname[:-3]+'dat', oldtifname[:-3]+'dat', oldoldtifname[:-3]+'dat')
	print gnuplotCmd
	proc.stdin.write(gnuplotCmd)      
	oldoldtifname = oldtifname
	oldtifname = tifname

#quit gnuplot
proc.stdin.write('quit\n')
