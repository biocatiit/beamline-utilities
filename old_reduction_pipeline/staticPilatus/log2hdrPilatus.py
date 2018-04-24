# -*- coding: utf-8 -*-
import sys
import os

#logname = sys.argv[1]
logname = '/home/weifeng/SAXS-data/20131129Shang/header/cytc.log'
headerPath = '/home/weifeng/SAXS-data/20131129Shang/header/'

with open(logname, 'r') as f:
    title = f.readline() # ignore the 1st title line
    linenumber = 0
    for line in f:
      txtline = line.rstrip()
      if txtline:
        columns = line.split()
        #tifname = columns[0] + '.txt'
        incident = columns[1]
        transmitted = columns[2]
        exposure = columns[4]
        headerfname = 'cytc0001_%05d.txt' %linenumber
        fout = open(os.path.join(headerPath, headerfname), 'w')
        fout.writelines('Exposure time [s]: %s\n' %exposure)
        fout.writelines('Transmitted Beam: %s\n' %transmitted)
        fout.writelines('Incident Beam: %s\n' %incident)
        #fout.writelines('Code: %s\n' %logname[:-4])
        fout.writelines('Code: cone\n')
        fout.writelines('Concentration [mg/ml]: 1\n')
        fout.writelines('Run Number: %05d\n' %linenumber)
        fout.close
        linenumber += 1
        #print 'Output %s ... done!' %tifname
