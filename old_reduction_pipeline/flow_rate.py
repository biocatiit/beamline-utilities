# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sys

Tmax = float(sys.argv[1]) # in seconds
sample_thickness = float(sys.argv[2]) # in micron
sheath_thickness = float(sys.argv[3]) # in micron

totalArea = 200*1000 # um2
sampleArea = 600 * sample_thickness
sheathArea = 600 * sheath_thickness *2
bufferArea = totalArea - sampleArea - sheathArea

#print sampleArea, sheathArea, bufferArea

flow_velocity = 25/Tmax # mm/s
totalFlowRate = totalArea * flow_velocity/1E6 * 60 #mm3/s, uL/s
print 'Total flow rate: %.2f uL per minute' %totalFlowRate

sampleFlowRate = totalFlowRate * sampleArea/totalArea
print 'Sample flow rate: %.2f uL per minute' %sampleFlowRate
sheathFlowRate = totalFlowRate * sheathArea/totalArea
print 'Sheath flow rate: %.2f uL per minute' %sheathFlowRate
bufferFlowRate = totalFlowRate * bufferArea/totalArea
print 'Buffer flow rate: %.2f uL per minute' %bufferFlowRate
