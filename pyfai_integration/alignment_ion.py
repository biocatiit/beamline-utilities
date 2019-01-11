import numpy as np
import matplotlib.pyplot as plt
import sys
import glob
import os.path

header_path = '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/cytc/20181202/'
header_prefix = 'b-cytc'

flist = glob.glob(os.path.join(header_path, '{}*.ion'.format(header_prefix)))

header_data = []

for i, f in enumerate(flist):
    print(f)

    point, time, i0, i1, junk1, junk2, x, y = np.loadtxt(f, delimiter=',', unpack=True)

    trans = i1/i0

    header_data.append([f, point, trans, x, y])


ref_data = header_data.pop(0)
