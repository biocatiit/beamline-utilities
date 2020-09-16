import os.path
import argparse
import glob

import hdf5plugin
import fabio

parser = argparse.ArgumentParser(description='Conversion of Eiger hdf5 (.h5) data to tif')
parser.add_argument('target', help='The target file for conversion (can be multile files providing just a common prefix)')
parser.add_argument('-o', '--output-dir', metavar='DIR', dest='output_dir', help='The output directory for .tif files (default: same directory as target)')

args = parser.parse_args()

data_files = args.target
data_files = os.path.expanduser(data_files)
data_files = os.path.abspath(data_files)

if not os.path.isfile(data_files):
    data_files = glob.glob(data_files+'*_master.h5')
else:
    data_files = [data_files]

if args.output_dir is not None:
    output_dir = args.output_dir
else:
    output_dir = os.path.split(data_files[0])[0]

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for data_file in data_files:
    fabio_img = fabio.open(data_file)

    data_prefix = os.path.splitext(os.path.split(data_file)[1])[0]

    print 'Input data file is: {}'.format(data_file)

    for i in range(fabio_img.nframes):
        print 'Converting image {} of {}'.format(i+1, fabio_img.nframes)
        data = fabio_img.data
        header = fabio_img.getheader()
        tif = fabio.pilatusimage.pilatusimage(header=header, data=data)
        tif.write(os.path.join(output_dir, data_prefix+'_{:05d}.tif'.format(i+1)))

        if i < fabio_img.nframes -1:
            fabio_img = fabio_img.next()
