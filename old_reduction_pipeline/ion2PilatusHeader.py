# -*- coding: utf-8 -*-
import sys
import os

logpath = '/home/biocat/SAXS_logs/2014run1/Osman_2014_0209/'
headerPath = '/home/biocat/SAXS_data/Osman_20140208/header/'

scanNumber = 100
frameNumber = 56
rootFileName = sys.argv[1] #'cytca'

for scan in range(0, scanNumber):
  logname = rootFileName + '_%04d.ion.csv' %(scan+1)
  print logname
  with open(os.path.join(logpath, logname), 'r') as f:
    for line in f:
      txtline = line.rstrip()
      if txtline:
        columns = line.split()
        frame = int(float(columns[0][:-1]))
        incident = columns[2][:-1]
        transmitted = columns[3][:-1]
        headerfname = rootFileName + '%04d_%05d.txt' %(scan+1, frame-1)
        #print headerfname

        fout = open(os.path.join(headerPath, headerfname), 'w')
        fout.writelines('Exposure time [s]: 0.19\n')
        fout.writelines('Transmitted Beam: %s\n' %transmitted)
        fout.writelines('Incident Beam: %s\n' %incident)
        fout.writelines('Code: cytc_unf%04d\n' %(scan+1))
        fout.writelines('Concentration [mg/ml]: 1\n')
        fout.writelines('Run Number: %05d\n' %frame)
        fout.close
        print 'Output %s ... done!' %headerfname
