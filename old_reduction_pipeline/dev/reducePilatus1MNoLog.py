# -*- coding: utf-8 -*-
import time
import glob
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import Image

parameterFile = sys.argv[1]
fileRootName = sys.argv[2]

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


def convertLog2Header(logfile):
  print logfile
  os.chdir(headerPath)
  rawLogFile = os.path.join(logPath, logfile)
  clonedLogFile = os.path.join(headerPath, logfile)
  os.system('cp %s %s' %(rawLogFile, clonedLogFile))
  with open(clonedLogFile, 'r') as f:
    title = f.readline() # ignore the 1st title line
    for line in f:
      columns = line.split()
      print columns
      print len(columns)
      try:
        headername = columns[0]
        incident = columns[1]
        transmitted = columns[2]
        I1overI0 = columns[3]
        exposure = columns[4]
        
        fout = open(headername + '.txt', 'w')
        fout.writelines('Exposure time [s]: %s\n' %exposure)
        #fout.writelines('Transmitted Beam: %s\n' %transmitted)
        fout.writelines('Transmitted Beam: %s\n' %incident)
        fout.writelines('Incident Beam: %s\n' %incident)
        fout.writelines('Code: %s\n' %headername[:-5])
        fout.writelines('Concentration [mg/ml]: 1\n')
        fout.writelines('Run Number: %s\n' %headername[-4:])
        fout.close
        print 'Header file: ' + headername + '.txt created!'
      except:
        print 'Warning: corrupted entry in the log file! Entry skipped!'

#open gnuplot
proc = subprocess.Popen(['gnuplot', '-p'], shell = True, stdin=subprocess.PIPE,)
proc.stdin.write('set log x\n')
proc.stdin.write('set log y\n')
proc.stdin.write('set xrange [0.004:0.4]\n')
proc.stdin.write("cd '%s'\n" %datPath)

oldtifname = 'old.dat'
oldoldtifname = 'oldold.dat'

plt.ion() #turn on interactive mode on plot
while True:
  newlist = sorted(glob.glob(tifPath + fileRootName + '_*.tif'))
  #print newlist
  for tif in newlist:
    path, tifname = os.path.split(tif)
    
    if not os.path.isfile(os.path.join(datPath, tifname[:-3] + 'dat')):
      #if not os.path.isfile(os.path.join(headerPath,  tifname[:-3] + 'txt')):
      #  convertLog2Header(tifname[:-9] + '.log')
      #print os.path.join(headerPath,  tifname[:-3] + 'txt')
      #if os.path.isfile(os.path.join(headerPath,  tifname[:-3] + 'txt')):
        # make sure header file exist. e.g. the last frame, tif exists but not in log
        os.chdir(datPath)
        #radaverCommand = 'radaver -x %.2f -y %.2f --beamstop-mask=%s --axis-data=%s %s %s' %(beamCenterX, beamCenterY, fit2dmask, qaxis,  headerPath + tifname[:-3] + 'txt', tif)
        ##################### plot the tif image ######
        #print tif
        im = Image.open(tif)
        imArray = np.array(im)
        plt.title(tif)
        plt.imshow(np.log10(imArray))
        plt.draw()
        ###################### plot updated ###########
        #command radaver without header file
        radaverCommand = 'radaver -x %.2f -y %.2f --beamstop-mask=%s --axis-data=%s %s' %(beamCenterX, beamCenterY, fit2dmask, qaxis, tif)
        os.system(radaverCommand)
        time.sleep(1)
        print(radaverCommand)
        print tifname + ' ---> ' + tifname[:-3] + 'dat done;'
        gnuplotCmd = "plot '%s' u 1:2:3 w yerrorbars, '%s' u 1:2 w l, '%s' u 1:2 w l\n" % (tifname[:-3]+'dat', oldtifname[:-3]+'dat', oldoldtifname[:-3]+'dat')
        print gnuplotCmd
        proc.stdin.write(gnuplotCmd)      
        oldoldtifname = oldtifname
        oldtifname = tifname
    print 'Press Ctrl+C to exit!'
    time.sleep(0.1)
  time.sleep(0.5)

#quit gnuplot
proc.stdin.write('quit\n')
