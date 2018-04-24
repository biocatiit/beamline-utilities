# -*- coding: utf-8 -*-
import glob
import os
import sys
import time
parameterFile = sys.argv[1]
#fileRootName = sys.argv[2]

parameter = {}
execfile (parameterFile, parameter)

# USER SETTINGS START #
#### Set correct directories ####

tifPath = parameter["tifPath"]

import matplotlib.pyplot as plt
import numpy as np
import Image
plt.ion()
while True:
  newest = max(glob.iglob(tifPath + '*_*.tif'), key = os.path.getctime)
  print newest
  im = Image.open(newest)
  imArray = np.array(im)
  plt.title(newest)
  plt.imshow(np.log10(imArray))
  plt.draw()
  print "Press Ctrl+C to stop!"
  time.sleep(2)

