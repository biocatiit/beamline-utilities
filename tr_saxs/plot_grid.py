import numpy as np
import matplotlib.pyplot as plt
import sys

fname = sys.argv[1]

if len(sys.argv)>2:
    plottype = sys.argv[2]
else:
    plottype = 'grid'


x, y, i = np.loadtxt(fname, delimiter=',', unpack=True)

cens = []
pos = []

x_vals = np.array(sorted(list(set(x))))
y_vals = np.array(sorted(list(set(y))))
i_vals = np.array(i, dtype=float).reshape((y_vals.size, x_vals.size))

if x[0] > x[-1]:
    i_vals = i_vals[:,::-1]
    x_vals = x_vals[::-1]
if y[0] > y[1]:
    i_vals = i_vals[::-1,:]
    y_vals = y_vals[::-1]

if plottype == 'grid':
    plt.imshow(i_vals, extent=[x_vals[0], x_vals[-1], y_vals[0], y_vals[-1]], aspect='auto')

elif plottype == 'x':
    center_positions = []
    for i, y in enumerate(y_vals):
        max_pos = np.argmax(i_vals[i,:])
        max_val = i_vals[i,:][max_pos]

        side1 = np.where(i_vals[i,:]>max_val*.8)[0][0]
        side2 = np.where(i_vals[i,:]>max_val*.8)[0][-1]
        cen_pos = int((side2+side1)/2)

        center_positions.append(cen_pos)

        plt.plot(x_vals, i_vals[i,:], label='Y={}, Center={}'.format(y, cen_pos))

elif plottype == 'y':
    center_positions = []
    for i, x in enumerate(x_vals):
        max_pos = np.argmax(i_vals[:,i])
        max_val = i_vals[:,i][max_pos]

        side1 = np.where(i_vals[:,i]>max_val*.8)[0][0]
        side2 = np.where(i_vals[:,i]>max_val*.8)[0][-1]
        cen_pos = int((side2+side1)/2)

        center_positions.append(cen_pos)

        plt.plot(y_vals, i_vals[:,i], label='X={}, Center={}'.format(x, cen_pos))

if plottype == 'y' or plottype == 'x':
    plt.legend()

plt.show()
