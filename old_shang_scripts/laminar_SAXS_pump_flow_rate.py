# -*- coding: utf-8 -*-
import sys

print '\n Usage: python flowrate.py Tmax(in ms) sample_sheet_thickness(in micron) sheath_thickness(in micron)\n'

Tmax = float(sys.argv[1])/1000. # in seconds
sample_thickness = float(sys.argv[2]) # in micron
sheath_thickness = float(sys.argv[3]) # in micron

totalArea = 200*1000 # um2
sampleArea = 600 * sample_thickness
sheathArea = 600 * sheath_thickness *2
bufferArea = int(totalArea) - int(sampleArea) - int(sheathArea)

#print sampleArea, sheathArea, bufferArea

flow_velocity = 25/Tmax # mm/s
totalFlowRate = totalArea * flow_velocity/1E6 #mm3/s, uL/s
print 'Total flow rate: %.2f uL per second' %totalFlowRate

sampleFlowRate = totalFlowRate * sampleArea/totalArea*60/1000.
print 'Sample flow rate: %.3f mL per minute' %sampleFlowRate

sheathFlowRate = totalFlowRate * sheathArea/totalArea * 60/1000.
print 'Sheath flow rate: %.3f mL per minute' %sheathFlowRate

bufferFlowRate = totalFlowRate * bufferArea/totalArea * 60/1000.
print 'Buffer flow rate: %.3f mL per minute' %bufferFlowRate

print '\nPump setting for Tmax = %d ms:\n' %(Tmax*1000)
print 'Pump 0 (side pump): %.3f mL per minute' %(bufferFlowRate/2.) 
print 'Pump 1 (diagonal pump): %.3f mL per minute' %(sheathFlowRate/2.) 
print 'Pump 2 (sample pump): %.3f mL per minute' %sampleFlowRate

print '\nSyringe volume for 30 minutes of continuous flow\n'
print 'Pump 0 : %.3f mL' %(bufferFlowRate*30/2.)
print 'Pump 1 : %.3f mL' %(sheathFlowRate*30/2.) 
print 'Pump 2 : %.3f mL' %(sampleFlowRate*30.)
