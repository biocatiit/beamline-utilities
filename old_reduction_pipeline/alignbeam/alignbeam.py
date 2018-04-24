import os
import sys
import datetime
import time

from epics import *

# Pilatus 1M PV
PV_PILATUS1M = '18IDpil1M:cam1:'
acquire_pv = PV(PV_PILATUS1M + 'Acquire')
pv_ExposureTime = PV(PV_PILATUS1M + 'AcquireTime')
pv_AcquirePeriod = PV(PV_PILATUS1M + 'AcquirePeriod')
pv_NumImages = PV(PV_PILATUS1M + 'NumImages')
pv_FileName= PV(PV_PILATUS1M + 'FileName')
pv_FullFileName= PV(PV_PILATUS1M + 'FullFileName_RBV')
pv_FileNumber= PV(PV_PILATUS1M + 'FileNumber')

fName = 'alignbeam'
pv_ExposureTime.put(1.0)
pv_AcquirePeriod.put(1.1)
pv_NumImages.put(1)
pv_FileName.put(fName)
pv_FileNumber.put(1) # frame always start from 1

# start detector
acquire_pv.put(1)

fullpath = '/nas_data/Pilatus1M/20160615ShangAlignment'
tifname = os.path.join(fullpath, fName + '_0001.tif')
print tifname

sys.path.insert(0, "/usr/local/dectris/albula/3.2/python")
import dectris.albula as dec
m = dec.openMainFrame()
s = m.openSubFrame()
s.loadFile(tifname)
