import numpy as np
import matplotlib.pyplot as plt
import sys
import glob

base_fname = sys.argv[1]

if len(sys.argv)>2:
    plottype = sys.argv[2]
else:
    plottype = 'y'

flist = glob.glob(base_fname+'*.ion')

cens = []
pos = []

for i, f in enumerate(flist):
    print(f)
    point, time, i0, i1, junk1, junk2, x, y = np.loadtxt(f, delimiter=',', unpack=True)
    # print (x[0])
    if plottype == 'y':
        len_data = y
    else:
        len_data = x

    trans = i1/i0

    if i == 0:
        img = trans
    else:
        img = np.column_stack((img, trans))

    if plottype == 'y':
        # pos.append(x[0]+i)
        pos.append(x[0]+i*1)
    else:
        pos.append(y[0])


if plottype == 'y':
    plt.imshow(img, extent=[pos[0], pos[-1], y[0], y[-1]], aspect='auto')
else:
    plt.imshow(img, extent=[pos[0], pos[-1], x[0], x[-1]], aspect='auto')
# plt.title('Center positions')
# if plottype == 'y':
#     plt.xlabel('X distance (mm)')
#     plt.ylabel('Y center position')
# else:
#     plt.xlabel('Y distance (mm)')
#     plt.ylabel('X center position')

plt.show()