# Python script to renumber the cf-saxs data.
# Output format: basefilename_1234_1234.dat (scan#_frame#).
# To be used like a command line utility, run python renumber-with-scan-and-frame.py -h for options
#
# Try combining the dummy run with a "| more" to have a chance to parse the output
#

import os
import glob
import shutil
import argparse



def renum(source_dir, fprefix, frames, output_dir, dummy=False):

    print("Copying and renaming files with prefix {} from {} to {}".format(fprefix, source_dir, output_dir))

    file_list = glob.glob(os.path.join(source_dir, '{}*data*'.format(fprefix)))
    file_list.sort(key=lambda x: int(x.split('_')[-1].split('.')[0]))

    for f in file_list:
        path, filename = os.path.split(f)
        fname, ext = os.path.splitext(filename)

        temp_name = fname.split('_')
        base_file_name = '_'.join(temp_name[:-2])
        old_frame_num = int(temp_name[-1]) -1

        # base_file_name, old_frame_num = fname.split('_')
        # old_frame_num = int(old_frame_num) -1

        new_scan_num, new_frame_num = divmod(old_frame_num, frames)
        new_frame_num = new_frame_num + 1
        new_scan_num = new_scan_num + 1

        new_file_name = '{}_{:04d}_data_{:06d}{}'.format(base_file_name, new_scan_num, new_frame_num, ext)

        print("{} ===> {}".format(filename, new_file_name))

        if not dummy:
            shutil.copyfile(f, os.path.join(output_dir, new_file_name))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Copy and renumber time resolved data into scans')
    parser.add_argument('source_dir', help='The directory with the files')
    parser.add_argument('file_prefix',help='The file prefix to process')
    parser.add_argument('frames', help='The number of frames in each scan')
    parser.add_argument('-o', '--output-dir', metavar='DIR', dest='output_dir', help='The output directory for renamed files (default: source_dir)')
    parser.add_argument('-d', '--dummy', default=False, action='store_true', help='Use this flag to run a test, without copying or renaming files')

    args = parser.parse_args()

    source_dir = args.source_dir
    fprefix = args.file_prefix
    frames = int(args.frames)
    dummy = args.dummy

    if args.output_dir is not None:
        output_dir = args.output_dir
    else:
        output_dir = source_dir

    renum(source_dir, fprefix, frames, output_dir, dummy)
