import os
import glob
import shutil

from align_by_intensity import align_by_intensity

# batch list should be a list of lists. Each entry should be as:
# [source_dir, fprefix, frames, output_dir]
batch_list = [
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/cytc/20181201/a',
    # 'a-cytc',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_align/cytc/20181201/a'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/cytc/20181201/c',
    # 'c-cytc',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_align/cytc/20181201/c'
    # ],
    ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/cytc/20181201/d',
    'd-blank',
    '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_align/cytc/20181201/d'
    ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/cytc/20181202/a',
    # 'a-cytc',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_align/cytc/20181202/a'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/cytc/20181202/b',
    # 'b-cytc',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_align/cytc/20181202/b'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/cytc/20181202/c',
    # 'c-cytc',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_align/cytc/20181202/c'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/cytc/20181202/d',
    # 'd-cytc',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_align/cytc/20181202/d'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/cytc/20181202/e',
    # 'e-cytc',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_align/cytc/20181202/e'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/cytc/20181202/f',
    # 'f-cytc',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_align/cytc/20181202/f'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/cytc/20181202/g',
    # 'g-buffer',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_align/cytc/20181202/g'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/haas/a-akblank',
    # 'a-akblank',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_align/haas/a-akblank'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/haas/b-akprotein',
    # 'b-akprotein',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_align/haas/b-akprotein'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/haas/c-akblank',
    # 'c-akblank',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_align/haas/c-akblank'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/haas/d-akprotein',
    # 'd-akprotein',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_align/haas/d-akprotein'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/haas/e-cytcnat',
    # 'e-cytcnat',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_align/haas/e-cytcnat'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/haas/f-cytcnatp',
    # 'f-cytcnatp',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_align/haas/f-cytcnatp'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/sosnick/a-ubbf06',
    # 'a-ubbf06',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_align/sosnick/a-ubbf06'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/sosnick/b-ub06',
    # 'b-ub06',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_align/sosnick/b-ub06'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/sosnick/c-ub06',
    # 'c-ub06',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_align/sosnick/c-ub06'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/sosnick/d-ub04',
    # 'd-ub04',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_align/sosnick/d-ub04'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/sosnick/e-ub04',
    # 'e-ub04',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_align/sosnick/e-ub04'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/sosnick/g-ub20',
    # 'g-ub20',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_align/sosnick/g-ub20'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/sosnick/h-mbp02',
    # 'h-mbp02',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_align/sosnick/h-mbp02'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/sosnick/i-mbp02',
    # 'i-mbp02',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_align/sosnick/i-mbp02'
    # ],
]

for source_dir, fprefix, output_dir in batch_list:
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        flist = glob.glob(os.path.join(source_dir, '{}*.dat'.format(fprefix)))

        scan_nums = [int(os.path.splitext(os.path.basename(f))[0].split('_')[-2]) for f in flist]
        scan_nums = list(set(scan_nums))
        scan_nums.sort()

        ref_scan = scan_nums[0]

        offsets = []

        for scan_num in scan_nums[1:]:

            offset = align_by_intensity(source_dir, fprefix, ref_scan,
                source_dir, fprefix, scan_num, 'both', output_dir)

            offsets.append(offset)

        ref_scan_files = glob.glob(os.path.join(source_dir, '{}_{:04}_*.dat'.format(fprefix, ref_scan)))

        for f in ref_scan_files:
            shutil.copyfile(f, os.path.join(output_dir, os.path.basename(f)))

        new_flist = glob.glob(os.path.join(output_dir, '{}*.dat'.format(fprefix)))

        if 0 not in offsets:
            offsets.append(0)

        max_offset = max(offsets)
        min_offset = min(offsets)
        total_scan_num = len(ref_scan_files)

        for f in new_flist:
            fnum = int(os.path.splitext(os.path.basename(f))[0].split('_')[-1])

            if fnum < max_offset + 1:
                os.remove(f)
            elif fnum > total_scan_num + min_offset:
                os.remove(f)

    except KeyboardInterrupt:
        break
