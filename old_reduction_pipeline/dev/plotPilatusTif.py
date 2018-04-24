# -*- coding: utf-8 -*-
import Image
import numpy as np
import matplotlib.pyplot as plt
import time
import sys

pilatustif = sys.argv[1]
print pilatustif
plt.ion()

im = Image.open(pilatustif)
saxs = np.array(im)
plt.title(pilatustif)
plt.imshow(np.log10(saxs))
plt.draw()
time.sleep(3)
