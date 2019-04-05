import numpy as np
import matplotlib.pyplot as plt
import sys
import glob

base_fname = sys.argv[1]


if len(sys.argv)>2:
    plottype = sys.argv[2]
else:
    plottype = 'y'

flist = glob.glob(base_fname+'??.log')

flist = sorted(flist, key=lambda x: int(x.split('_')[-1].strip('.log')))

# flist = [flist[i] for i in range(0, len(flist), 10)]

for k, fname in enumerate(flist):
    print(fname)

    with open(fname,'rU') as f:
        all_lines=f.readlines()

    for i, line in enumerate(all_lines):
        if line.startswith('#Filename') or line.startswith('#image'):
            labels = line.strip('#\n').split('\t')
            offset = i

    vals = [[] for i in range(len(labels))]

    for i in range(offset+1, len(all_lines)):
        line = all_lines[i]

        for j, ctr in enumerate(line.strip().split('\t')):
            vals[j].append(ctr)

    log_values = {}

    for i, label in enumerate(labels):
        if label == 'Filename':
            log_values[label] = vals[i]
        else:
            log_values[label] = np.array(vals[i], dtype=float)

    x = log_values['x']
    y = log_values['y']
    i1 = log_values['I1']
    i0 = log_values['I0']

    if plottype == 'y':
        len_data = y
    else:
        len_data = x

    trans = i1/i0
    # trans = i1
    # trans = i0

    max_pos = np.argmax(trans)

    max_val = trans[max_pos]

    side1 = np.where(trans>max_val*.8)[0][0]
    side2 = np.where(trans>max_val*.8)[0][-1]

    cen_pos = int((side2+side1)/2)


    # plt.plot(len_data, trans/trans[50], label='{}, cen={}'.format(i, len_data[cen_pos]))
    plt.plot(len_data, trans, label='{}'.format(k))

plt.title('Intensity scan data')
plt.xlabel('%s distance (mm)' %(plottype))
plt.ylabel('I1/I0')
plt.legend()
plt.show()
