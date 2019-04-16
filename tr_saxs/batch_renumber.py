import os

from renumber_with_scan_and_frame import renum

nframes = 1988

# batch list should be a list of lists. Each entry should be as:
# [source_dir, fprefix, frames, output_dir]
batch_list = [
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/cytc/20181201',
    # 'a-cytc', nframes,
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/cytc/20181201/a'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/cytc/20181201',
    # 'c-cytc', nframes,
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/cytc/20181201/c'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/cytc/20181201',
    # 'd-blank', nframes,
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/cytc/20181201/d'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/cytc/20181202',
    # 'a-cytc', nframes,
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/cytc/20181202/a'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/cytc/20181202',
    # 'b-cytc', nframes,
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/cytc/20181202/b'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/cytc/20181202',
    # 'c-cytc', nframes,
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/cytc/20181202/c'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/cytc/20181202',
    # 'd-cytc', nframes,
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/cytc/20181202/d'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/cytc/20181202',
    # 'e-cytc', nframes,
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/cytc/20181202/e'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/cytc/20181202',
    # 'f-cytc', nframes,
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/cytc/20181202/f'
    # ],
    ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/cytc/20181202',
    'g-buffer', nframes,
    '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/cytc/20181202/g'
    ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/haas',
    # 'a-akblank', nframes,
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/haas/a-akblank'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/haas',
    # 'b-akprotein', nframes,
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/haas/b-akprotein'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/haas',
    # 'c-akblank', nframes,
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/haas/c-akblank'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/haas',
    # 'd-akprotein', nframes,
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/haas/d-akprotein'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/haas',
    # 'e-cytcnat', nframes,
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/haas/e-cytcnat'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/haas',
    # 'f-cytcnatp', nframes,
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/haas/f-cytcnatp'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/sosnick',
    # 'a-ubbf06', nframes,
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/sosnick/a-ubbf06'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/sosnick',
    # 'b-ub06', nframes,
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/sosnick/b-ub06'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/sosnick',
    # 'c-ub06', nframes,
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/sosnick/c-ub06'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/sosnick',
    # 'd-ub04', nframes,
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/sosnick/d-ub04'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/sosnick',
    # 'e-ub04', nframes,
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/sosnick/e-ub04'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/sosnick',
    # 'g-ub20', nframes,
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/sosnick/g-ub20'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/sosnick',
    # 'h-mbp02', nframes,
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/sosnick/h-mbp02'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/sosnick',
    # 'i-mbp02', nframes,
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/sosnick/i-mbp02'
    # ],
]

for source_dir, fprefix, frames, output_dir in batch_list:
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        renum(source_dir, fprefix, frames, output_dir)

    except KeyboardInterrupt:
        break
