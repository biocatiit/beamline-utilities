import numpy as np
import matplotlib.pyplot as plt
import sys

fname = sys.argv[1]

if len(sys.argv)>2:
    plottype = sys.argv[2]
else:
    plottype = 'y'

point, time, i0, i1, junk1, junk2, x, y = np.loadtxt(fname, delimiter=',', unpack=True)

if plottype == 'y':
    len_data = y
else:
    len_data = x

trans = i1/i0

max_pos = np.argmax(trans)

max_val = trans[max_pos]

side1 = np.where(trans>max_val*.8)[0][0]
side2 = np.where(trans>max_val*.8)[0][-1]

cen_pos = int((side2+side1)/2)

plt.plot(len_data, trans)
plt.title('Intensity scan data, center = %f' %(len_data[cen_pos]))
plt.xlabel('%s distance (mm)' %(plottype))
plt.ylabel('I1/I0')
plt.show()