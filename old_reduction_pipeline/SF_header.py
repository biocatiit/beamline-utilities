# -*- coding: utf-8 -*-
import sys

logname = sys.argv[1]
RootFileName = sys.argv[2] #'MgSAM_Buff'

cycle = 1 # 1-10
frame = 15

with open(logname, 'r') as f:
    title = f.readline() # ignore the 1st title line
    for line in f:
        columns = line.split()
        #tifname = columns[0] + '.txt'
        tifname = '%s%04d_%05d' %(RootFileName, cycle, frame)
        incident = columns[1]
        transmitted = columns[2]
        incident = columns[3]
        exposure = '1' #columns[4]
        fout = open(tifname, 'w')
        fout.writelines('Exposure time [s]: %s\n' %exposure)
        fout.writelines('Transmitted Beam: %s\n' %transmitted)
        fout.writelines('Incident Beam: %s\n' %incident)
        fout.writelines('Code: %s\n' %logname[:-4])
        fout.writelines('Concentration [mg/ml]: 1')
        fout.close
        print 'Output %s ... done!' %tifname
        cycle += 1
