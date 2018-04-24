import Image
import numpy as np

import sys
pilatustif = sys.argv[1]

im = Image.open(pilatustif)
saxs = np.array(im)

import matplotlib.pyplot as plt
plt.imshow(np.log10(saxs))
plt.show()
