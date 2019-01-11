import os
from normalize_dats import normalize_dats

# batch list should be a list of lists. Each entry should be as:
# [source_dir, fprefix, frames, output_dir]
batch_list = [
    ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/cytc/20181201/a',
    'a-cytc',
    '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/cytc/20181201/a'
    ],
    ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/cytc/20181201/c',
    'c-cytc',
    '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/cytc/20181201/c'
    ],
    ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/cytc/20181201/d',
    'd-blank',
    '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/cytc/20181201/d'
    ],
    ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/cytc/20181202/a',
    'a-cytc',
    '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/cytc/20181202/a'
    ],
    ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/cytc/20181202/b',
    'b-cytc',
    '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/cytc/20181202/b'
    ],
    ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/cytc/20181202/c',
    'c-cytc',
    '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/cytc/20181202/c'
    ],
    ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/cytc/20181202/d',
    'd-cytc',
    '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/cytc/20181202/d'
    ],
    ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/cytc/20181202/e',
    'e-cytc',
    '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/cytc/20181202/e'
    ],
    ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/cytc/20181202/f',
    'f-cytc',
    '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/cytc/20181202/f'
    ],
    ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/cytc/20181202/g',
    'g-buffer',
    '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/cytc/20181202/g'
    ],
    ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/haas/a-akblank',
    'a-akblank',
    '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/haas/a-akblank'
    ],
    ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/haas/b-akprotein',
    'b-akprotein',
    '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/haas/b-akprotein'
    ],
    ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/haas/c-akblank',
    'c-akblank',
    '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/haas/c-akblank'
    ],
    ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/haas/d-akprotein',
    'd-akprotein',
    '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/haas/d-akprotein'
    ],
    ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/haas/e-cytcnat',
    'e-cytcnat',
    '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/haas/e-cytcnat'
    ],
    ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/haas/f-cytcnatp',
    'f-cytcnatp',
    '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/haas/f-cytcnatp'
    ],
    ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/sosnick/a-ubbf06',
    'a-ubbf06',
    '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/sosnick/a-ubbf06'
    ],
    ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/sosnick/b-ub06',
    'b-ub06',
    '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/sosnick/b-ub06'
    ],
    ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/sosnick/c-ub06',
    'c-ub06',
    '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/sosnick/c-ub06'
    ],
    ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/sosnick/d-ub04',
    'd-ub04',
    '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/sosnick/d-ub04'
    ],
    ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/sosnick/e-ub04',
    'e-ub04',
    '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/sosnick/e-ub04'
    ],
    ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/sosnick/g-ub20',
    'g-ub20',
    '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/sosnick/g-ub20'
    ],
    ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/sosnick/h-mbp02',
    'h-mbp02',
    '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/sosnick/h-mbp02'
    ],
    ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/sosnick/i-mbp02',
    'i-mbp02',
    '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_norm_renum/sosnick/i-mbp02'
    ],
]

for source_dir, fprefix, output_dir in batch_list:
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        normalize_dats(source_dir, fprefix, output_dir)

    except KeyboardInterrupt:
        break
