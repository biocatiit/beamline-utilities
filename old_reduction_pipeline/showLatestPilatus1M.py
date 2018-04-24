import time
import glob
import os
import sys

parameterFile = sys.argv[1]

parameter = {}
execfile (parameterFile, parameter)

tifPath = parameter["tifPath"]

import sys
sys.path.insert(0,"/usr/local/dectris/albula/3.2/python") # or wherever you've installed ALBULA
import dectris.albula

m = dectris.albula.openMainFrame()
s = m.openSubFrame()

while 1:
	newest = max(glob.iglob(tifPath + '*.tif'), key=os.path.getctime)
	print newest
	s.loadFile(newest)
	time.sleep(1)
