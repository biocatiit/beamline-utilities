# -*- coding: utf-8 -*-
import time
import glob
import os
import sys
import numpy as np
import matplotlib.pyplot as plt


tifPath = '/mnt/detectors/Pilatus1M/20150128Startup/' #parameter["tifPath"]
fileRootName = 'align5m'
import Image
import numpy as np

newlist = sorted(glob.glob(tifPath + fileRootName + '_*.tif'))
  #print newlist
plt.ion()
for tif in newlist:
    print tif
    im = Image.open(tif)
    imArray = np.array(im)
    plt.imshow(np.log10(imArray))
    plt.draw()
    time.sleep(1)
