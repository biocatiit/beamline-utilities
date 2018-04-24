import time
import glob
import os
import sys

parameterFile = sys.argv[1]
image_prefix = sys.argv[2]

parameter = {}
execfile (parameterFile, parameter)

tifPath = parameter["tifPath"]
file_pattern = os.path.join(tifPath, image_prefix + '*.tif')
print file_pattern

import sys
sys.path.insert(0,"/usr/local/dectris/albula/3.2/python") # or wherever you've installed ALBULA
import dectris.albula

m = dectris.albula.openMainFrame()
s = m.openSubFrame()

all = sorted(glob.glob(file_pattern), key=os.path.getctime)
print all
for f in all:
	s.loadFile(f)
	#time.sleep(1)
	raw_input('Hit any key to open next image')
