import os
import glob
import shutil

def renum_scan_files(data_dir, fprefix, num_frames, total_runs, det_type, dummy=False):

    for current_run in range(1, total_runs+1):
        f_start = (int(current_run) - 1)*num_frames + 1

        if det_type == 'eiger':
            f_list = ['{}_data_{:06d}.h5'.format(fprefix, f_start+i) for i in range(num_frames)]
        elif det_type == 'pilatus':
            f_list = ['{}_{:06d}.tif'.format(fprefix, f_start+i) for i in range(num_frames)]

        timeout = False

        for i, f in enumerate(f_list):
            full_path = os.path.join(data_dir, f)

            if det_type == 'eiger':
                new_name = '{}_{:04d}_data_{:06d}.h5'.format(fprefix, int(current_run), i+1)
            elif det_type == 'pilatus':
                new_name = '{}_{:04d}_{:06d}.tif'.format(fprefix, int(current_run), i+1)

            full_new = os.path.join(data_dir, new_name)

            print(full_path)
            print(full_new)
            if os.path.exists(full_path):
                print('Moving %s to %s', full_path, full_new)
                if not dummy:
                    shutil.move(full_path, full_new)


if __name__ == '__main__':
    data_dir = '/nas_data/Pilatus1M/2026_1M/2026_Run1/2026_04_01_Grubic/TG01'
    fprefix = 'TG01'
    num_frames = 240
    total_runs = 160
    det_type = 'pilatus'

    print('here')

    renum_scan_files(data_dir, fprefix, num_frames, total_runs, det_type, dummy=True)
