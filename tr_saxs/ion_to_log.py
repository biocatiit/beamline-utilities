import os
import glob
import math
import argparse

import numpy as np

def load_ion(fname):

    point, time, i0, i1, pilatus_trig, shutter_trig, x, y = np.loadtxt(fname, delimiter=',', unpack=True)

    return point, time, i0, i1, pilatus_trig, shutter_trig, x, y

#This code to find the contiguous regions of the data is based on these
#questions from stack overflow:
#https://stackoverflow.com/questions/4494404/find-large-number-of-consecutive-values-fulfilling-condition-in-a-numpy-array
#https://stackoverflow.com/questions/12427146/combine-two-arrays-and-sort
def contiguous_regions(data):
    """Finds contiguous regions of the difference data. Returns
    a 1D array where each value represents a change in the condition."""

    if np.all(data==0):
        idx = np.array([])
    elif np.all(data>0) or np.all(data<0):
        idx = np.array([0, data.size])
    else:
        condition = data>0
        # Find the indicies of changes in "condition"
        d = np.ediff1d(condition.astype(int))
        idx, = d.nonzero()
        idx = idx+1

    return idx

def bin_ion(point, time, i0, i1, pilatus_trig, shutter_trig, x, y, subtract_offset=True, fnum_offset=0):
    index_array = contiguous_regions(pilatus_trig)

    if subtract_offset:
        shutter_index_array = contiguous_regions(shutter_trig)
        i0_offset = i0[:shutter_index_array[0]].mean()
        i1_offset = i1[:shutter_index_array[0]].mean()

        i0 = i0 - i0_offset
        i1 = i1 - i1_offset

    img_data = []

    for j in range(0, len(index_array), 2):
        start_idx = index_array[j]
        stop_idx = index_array[j+1]

        start_time = time[start_idx]
        exp_time = time[stop_idx] - time[start_idx]
        exp_i0 = i0[start_idx:stop_idx].sum()
        exp_i1 = i1[start_idx:stop_idx].sum()
        exp_x = x[start_idx:stop_idx].mean()
        exp_y = y[start_idx:stop_idx].mean()
        dist = math.sqrt((exp_x-x[0])**2+(exp_y-y[0])**2)


        img_num = len(img_data)+1+fnum_offset

        img_data.append([img_num, start_time, exp_time, exp_i0, exp_i1, exp_x, exp_y, dist])

    return img_data


def ion_to_scanlog(source_dir, fprefix, output_dir):
    flist = glob.glob(os.path.join(source_dir, '{}*.ion'.format(fprefix)))
    flist.sort(key=lambda x: int(x.split('_')[-1].split('.')[0]))

    for fname in flist:
        print('Processing {}'.format(os.path.basename(fname)))
        point, time, i0, i1, pilatus_trig, shutter_trig, x, y = load_ion(fname)

        img_data = bin_ion(point, time, i0, i1, pilatus_trig, shutter_trig, x, y)

        prefix = os.path.splitext(os.path.basename(fname))[0]
        log_name = '{}.log'.format(prefix)
        log_name = os.path.join(output_dir, log_name)

        with open(log_name, 'w') as f:
            f.write('#Filename\tstart_time\texposure_time\tI0\tI1\tx_pos_(mm)\ty_pos_(mm)\tdistance_(mm)\n')
            for data in img_data:
                f.write('{}_{:04}.tif\t{}\n'.format(prefix, data[0], '\t'.join(map(str, data[1:]))))

def ion_to_fulllog(source_dir, fprefix, output_dir):
    flist = glob.glob(os.path.join(source_dir, '{}*.ion'.format(fprefix)))
    flist.sort(key=lambda x: int(x.split('_')[-1].split('.')[0]))

    img_data = []

    for fname in flist:
        print('Processing {}'.format(os.path.basename(fname)))
        point, time, i0, i1, pilatus_trig, shutter_trig, x, y = load_ion(fname)

        binned = bin_ion(point, time, i0, i1, pilatus_trig, shutter_trig, x, y, fnum_offset=len(img_data))
        img_data = img_data + binned

    log_name = '{}.log'.format(fprefix)
    log_name = os.path.join(output_dir, log_name)

    with open(log_name, 'w') as f:
        f.write('#Filename\tstart_time\texposure_time\tI0\tI1\tx_pos_(mm)\ty_pos_(mm)\tdistance_(mm)\n')
        for data in img_data:
            f.write('{}_{:05}.tif\t{}\n'.format(fprefix, data[0], '\t'.join(map(str, data[1:]))))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parse .ion files from TR-SAXS experiments into standard BioCAT .log files')
    parser.add_argument('source_dir', help='The directory with the files')
    parser.add_argument('file_prefix',help='The file prefix to process')
    parser.add_argument('-o', '--output-dir', metavar='DIR', dest='output_dir', help='The output directory for renamed files (default: source_dir)')
    parser.add_argument('-f', '--full', default=False, action='store_true', help='Use to process all scan files into a single log file (useful for processing raw images)')

    args = parser.parse_args()

    source_dir = args.source_dir
    fprefix = args.file_prefix
    full = args.full

    if args.output_dir is not None:
        output_dir = args.output_dir
    else:
        output_dir = source_dir

    if full:
        ion_to_fulllog(source_dir, fprefix, output_dir)
    else:
        ion_to_scanlog(source_dir, fprefix, output_dir)



