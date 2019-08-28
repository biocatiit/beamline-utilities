import os

from ion_to_log import ion_to_fulllog, ion_to_scanlog

# batch list should be a list of lists. Each entry should be as:
# [source_dir, fprefix, log type, output_dir]
# log type is: scan - for individual scan logs
#              full - for all image logs
#              both - to do both
batch_list = [
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/cytc/20181201',
    # 'a-cytc', 'scan',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/cytc/20181201/a'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/cytc/20181201',
    # 'c-cytc', 'scan',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/cytc/20181201/c'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/cytc/20181201',
    # 'd-blank', 'scan',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/cytc/20181201/d'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/cytc/20181202',
    # 'a-cytc', 'scan',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/cytc/20181202/a'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/cytc/20181202',
    # 'b-cytc', 'scan',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/cytc/20181202/b'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/cytc/20181202',
    # 'c-cytc', 'scan',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/cytc/20181202/c'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/cytc/20181202',
    # 'd-cytc', 'scan',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/cytc/20181202/d'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/cytc/20181202',
    # 'e-cytc', 'scan',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/cytc/20181202/e'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/cytc/20181202',
    # 'f-cytc', 'scan',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/cytc/20181202/f'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/cytc/20181202',
    # 'g-buffer', 'scan',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/cytc/20181202/g'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/haas',
    # 'a-akblank', 'scan',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/haas/a-akblank'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/haas',
    # 'b-akprotein', 'scan',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/haas/b-akprotein'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/haas',
    # 'c-akblank', 'scan',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/haas/c-akblank'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/haas',
    # 'd-akprotein', 'scan',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/haas/d-akprotein'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/haas',
    # 'e-cytcnat', 'scan',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/haas/e-cytcnat'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/haas',
    # 'f-cytcnatp', 'scan',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/haas/f-cytcnatp'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/sosnick',
    # 'a-ubbf06', 'scan',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/sosnick/a-ubbf06'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/sosnick',
    # 'b-ub06', 'scan',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/sosnick/b-ub06'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/sosnick',
    # 'c-ub06', 'scan',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/sosnick/c-ub06'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/sosnick',
    # 'd-ub04', 'scan',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/sosnick/d-ub04'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/sosnick',
    # 'e-ub04', 'scan',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/sosnick/e-ub04'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/sosnick',
    # 'f-ub12', 'scan',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/sosnick/f-ub12'
    # ],
    ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/sosnick',
    'g-ub20', 'scan',
    '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/sosnick/g-ub20'
    ],
    ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/sosnick',
    'h-mbp02', 'scan',
    '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/sosnick/h-mbp02'
    ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/sosnick',
    # 'i-mbp02', 'scan',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats_renum/sosnick/i-mbp02'
    # ],
]

# batch_list = [
#     ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/cytc/20181201',
#     'a-cytc', 'full',
#     '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/cytc/20181201'
#     ],
#     ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/cytc/20181201',
#     'c-cytc', 'full',
#     '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/cytc/20181201'
#     ],
#     ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/cytc/20181201',
#     'd-blank', 'full',
#     '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/cytc/20181201'
#     ],
#     ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/cytc/20181202',
#     'a-cytc', 'full',
#     '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/cytc/20181202'
#     ],
#     ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/cytc/20181202',
#     'b-cytc', 'full',
#     '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/cytc/20181202'
#     ],
#     ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/cytc/20181202',
#     'c-cytc', 'full',
#     '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/cytc/20181202'
#     ],
#     ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/cytc/20181202',
#     'd-cytc', 'full',
#     '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/cytc/20181202'
#     ],
#     ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/cytc/20181202',
#     'e-cytc', 'full',
#     '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/cytc/20181202'
#     ],
#     ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/cytc/20181202',
#     'f-cytc', 'full',
#     '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/cytc/20181202'
#     ],
#     ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/cytc/20181202',
#     'g-buffer', 'full',
#     '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/cytc/20181202'
#     ],
#     ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/haas',
#     'a-akblank', 'full',
#     '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/haas/'
#     ],
#     ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/haas',
#     'b-akprotein', 'full',
#     '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/haas/'
#     ],
#     ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/haas',
#     'c-akblank', 'full',
#     '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/haas/'
#     ],
#     ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/haas',
#     'd-akprotein', 'full',
#     '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/haas/'
#     ],
#     ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/haas',
#     'e-cytcnat', 'full',
#     '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/haas/'
#     ],
#     ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/haas',
#     'f-cytcnatp', 'full',
#     '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/haas/'
#     ],
#     ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/sosnick',
#     'a-ubbf06', 'full',
#     '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/sosnick/'
#     ],
#     ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/sosnick',
#     'b-ub06', 'full',
#     '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/sosnick/'
#     ],
#     ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/sosnick',
#     'c-ub06', 'full',
#     '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/sosnick/'
#     ],
#     ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/sosnick',
#     'd-ub04', 'full',
#     '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/sosnick/'
#     ],
#     ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/sosnick',
#     'e-ub04', 'full',
#     '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/sosnick/'
#     ],
#     ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/sosnick',
#     'g-ub20', 'full',
#     '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/sosnick/'
#     ],
#     ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/sosnick',
#     'h-mbp02', 'full',
#     '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/sosnick/'
#     ],
#     ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/headers/sosnick',
#     'i-mbp02', 'full',
#     '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/sosnick/'
#     ],
# ]

for source_dir, fprefix, log_type, output_dir in batch_list:
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        if log_type == 'full':
            ion_to_fulllog(source_dir, fprefix, output_dir)
        elif log_type == 'scan':
            ion_to_scanlog(source_dir, fprefix, output_dir)
        elif log_type == 'both':
            ion_to_fulllog(source_dir, fprefix, output_dir)
            ion_to_scanlog(source_dir, fprefix, output_dir)

    except KeyboardInterrupt:
        break
