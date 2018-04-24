from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import time
import sys

pilatustif = sys.argv[1]

im = Image.open(pilatustif)
saxs = np.array(im)

plt.ion()
plt.imshow(np.log10(saxs))
plt.draw()
time.sleep(3)
plt.close()
