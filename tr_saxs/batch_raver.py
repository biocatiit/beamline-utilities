import os
os.sys.path.append(os.path.abspath('../pyfai_integration/'))

import saxs_raver

cfg_file = '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/processing/mask_minq_0p016.cfg'

# batch list should be a list of lists. Each entry should be as:
# [source_dir, fprefix, output_dir]
# Note that if fprefix is None, all files in the directory will be processed

batch_list = [
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/cytc/20181201/',
    # 'a-cytc',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/cytc/20181201/'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/cytc/20181201/',
    # 'c-cytc',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/cytc/20181201/'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/cytc/20181201/',
    # 'd-blank',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/cytc/20181201/'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/cytc/20181202/',
    # 'a-cytc',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/cytc/20181202/'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/cytc/20181202/',
    # 'b-cytc',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/cytc/20181202/'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/cytc/20181202/',
    # 'c-cytc',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/cytc/20181202/'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/cytc/20181202/',
    # 'd-cytc',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/cytc/20181202/'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/cytc/20181202/',
    # 'e-cytc',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/cytc/20181202/'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/cytc/20181202/',
    # 'f-cytc',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/cytc/20181202/'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/cytc/20181202/',
    # 'g-buffer',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/cytc/20181202/'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/haas/',
    # 'a-akblank',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/haas'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/haas/',
    # 'b-akprotein',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/haas'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/haas/',
    # 'c-akblank',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/haas'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/haas/',
    # 'd-akprotein',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/haas'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/haas/',
    # 'e-cytcnat',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/haas'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/haas/',
    # 'f-cytcnatp',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/haas'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/sosnick/',
    # 'a-ubbf06',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/sosnick'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/sosnick/',
    # 'b-ub06',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/sosnick'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/sosnick/',
    # 'c-ub06',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/sosnick'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/sosnick/',
    # 'd-ub04',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/sosnick'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/sosnick/',
    # 'e-ub04',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/sosnick'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/sosnick/',
    # 'g-ub20',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/sosnick'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/sosnick/',
    # 'h-mbp02',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/sosnick'
    # ],
    # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/sosnick/',
    # 'i-mbp02',
    # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/sosnick'
    # ],
]


ai, mask, q_range, maxlen, normlist, do_normalization, raw_settings, calibrate_dict, fliplr, flipud = saxs_raver.init_integration(cfg_file)

start_point = raw_settings.get('StartPoint')
end_point = raw_settings.get('EndPoint')


for source_dir, fprefix, output_dir in batch_list:
    try:
        old_dir_list_dict = {}

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        diff_list, old_dir_list_dict = saxs_raver.getNewFiles(source_dir, old_dir_list_dict, fprefix)

        [saxs_raver.doIntegration(output_dir, ai, mask, q_range, maxlen, normlist,
        do_normalization, calibrate_dict, start_point, end_point, fliplr, flipud,
        os.path.join(source_dir, name)) for name, stuff in diff_list]

    except KeyboardInterrupt:
        break
