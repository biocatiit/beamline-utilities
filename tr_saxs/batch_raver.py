import os
os.sys.path.append(os.path.abspath('../pyfai_integration/'))

import saxs_raver

# cfg_file = '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/processing/mask_minq_0p016.cfg'

# # batch list should be a list of lists. Each entry should be as:
# # [source_dir, fprefix, output_dir]
# # Note that if fprefix is None, all files in the directory will be processed

# batch_list = [
#     # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/cytc/20181201/',
#     # 'a-cytc',
#     # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/cytc/20181201/'
#     # ],
#     # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/cytc/20181201/',
#     # 'c-cytc',
#     # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/cytc/20181201/'
#     # ],
#     # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/cytc/20181201/',
#     # 'd-blank',
#     # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/cytc/20181201/'
#     # ],
#     # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/cytc/20181202/',
#     # 'a-cytc',
#     # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/cytc/20181202/'
#     # ],
#     # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/cytc/20181202/',
#     # 'b-cytc',
#     # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/cytc/20181202/'
#     # ],
#     # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/cytc/20181202/',
#     # 'c-cytc',
#     # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/cytc/20181202/'
#     # ],
#     # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/cytc/20181202/',
#     # 'd-cytc',
#     # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/cytc/20181202/'
#     # ],
#     # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/cytc/20181202/',
#     # 'e-cytc',
#     # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/cytc/20181202/'
#     # ],
#     # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/cytc/20181202/',
#     # 'f-cytc',
#     # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/cytc/20181202/'
#     # ],
#     # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/cytc/20181202/',
#     # 'g-buffer',
#     # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/cytc/20181202/'
#     # ],
#     # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/haas/',
#     # 'a-akblank',
#     # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/haas'
#     # ],
#     # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/haas/',
#     # 'b-akprotein',
#     # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/haas'
#     # ],
#     # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/haas/',
#     # 'c-akblank',
#     # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/haas'
#     # ],
#     # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/haas/',
#     # 'd-akprotein',
#     # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/haas'
#     # ],
#     # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/haas/',
#     # 'e-cytcnat',
#     # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/haas'
#     # ],
#     # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/haas/',
#     # 'f-cytcnatp',
#     # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/haas'
#     # ],
#     # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/sosnick/',
#     # 'a-ubbf06',
#     # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/sosnick'
#     # ],
#     # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/sosnick/',
#     # 'b-ub06',
#     # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/sosnick'
#     # ],
#     # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/sosnick/',
#     # 'c-ub06',
#     # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/sosnick'
#     # ],
#     # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/sosnick/',
#     # 'd-ub04',
#     # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/sosnick'
#     # ],
#     # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/sosnick/',
#     # 'e-ub04',
#     # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/sosnick'
#     # ],
#     # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/sosnick/',
#     # 'f-ub12',
#     # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/sosnick'
#     # ],
#     # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/sosnick/',
#     # 'g-ub20',
#     # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/sosnick'
#     # ],
#     # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/sosnick/',
#     # 'h-mbp02',
#     # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/sosnick'
#     # ],
#     ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/sosnick_fix/',
#     'g-ub20',
#     '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/sosnick'
#     ],
#     ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/sosnick_fix/',
#     'h-mbp02',
#     '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/sosnick'
#     ],
#     # ['/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/sosnick/',
#     # 'i-mbp02',
#     # '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/dats/sosnick'
#     # ],
# ]


# #March 2019
# cfg_file = '/nas_data/Pilatus1M/20190326Hopkins/SAXS_fullmask0p015.cfg'

# # batch list should be a list of lists. Each entry should be as:
# # [source_dir, fprefix, output_dir]
# # Note that if fprefix is None, all files in the directory will be processed

# batch_list = [
#     # ['/nas_data/Pilatus1M/20190326Hopkins/cytc/cytc2/',
#     # 'cytc2',
#     # '/nas_data/Pilatus1M/20190326Hopkins/reproc_0p015_dats/cytc/cytc2'
#     # ],
#     # ['/nas_data/Pilatus1M/20190326Hopkins/cytc/cytc3/',
#     # 'cytc3',
#     # '/nas_data/Pilatus1M/20190326Hopkins/reproc_0p015_dats/cytc/cytc3'
#     # ],
#     # ['/nas_data/Pilatus1M/20190326Hopkins/cytc/cytc4/',
#     # 'cytc4',
#     # '/nas_data/Pilatus1M/20190326Hopkins/reproc_0p015_dats/cytc/cytc4'
#     # ],
#     # ['/nas_data/Pilatus1M/20190326Hopkins/cytc/cytc5/',
#     # 'cytc5',
#     # '/nas_data/Pilatus1M/20190326Hopkins/reproc_0p015_dats/cytc/cytc5'
#     # ],
#     # ['/nas_data/Pilatus1M/20190326Hopkins/cytc/cytc6/',
#     # 'cytc6',
#     # '/nas_data/Pilatus1M/20190326Hopkins/reproc_0p015_dats/cytc/cytc6'
#     # ],
#     # ['/nas_data/Pilatus1M/20190326Hopkins/cytc/cytc7/',
#     # 'cytc7',
#     # '/nas_data/Pilatus1M/20190326Hopkins/reproc_0p015_dats/cytc/cytc7'
#     # ],
#     # ['/nas_data/Pilatus1M/20190326Hopkins/cytc/cytc8/',
#     # 'cytc8',
#     # '/nas_data/Pilatus1M/20190326Hopkins/reproc_0p015_dats/cytc/cytc8'
#     # ],
#     # ['/nas_data/Pilatus1M/20190326Hopkins/cytc/cytc9/',
#     # 'cytc9',
#     # '/nas_data/Pilatus1M/20190326Hopkins/reproc_0p015_dats/cytc/cytc9'
#     # ],
#     # ['/nas_data/Pilatus1M/20190326Hopkins/cytc/cytc10/',
#     # 'cytc10',
#     # '/nas_data/Pilatus1M/20190326Hopkins/reproc_0p015_dats/cytc/cytc10'
#     # ],
#     # ['/nas_data/Pilatus1M/20190326Hopkins/cytc/cytc10/',
#     # 'cytc10',
#     # '/nas_data/Pilatus1M/20190326Hopkins/reproc_0p015_dats/cytc/cytc10'
#     # ],
#     ['/nas_data/Pilatus1M/20190326Hopkins/cytc/buffer2/',
#     'buffer2',
#     '/nas_data/Pilatus1M/20190326Hopkins/reproc_0p015_dats/cytc/buffer2'
#     ],
#     ['/nas_data/Pilatus1M/20190326Hopkins/cytc/buffer3/',
#     'buffer3',
#     '/nas_data/Pilatus1M/20190326Hopkins/reproc_0p015_dats/cytc/buffer3'
#     ],
#     ['/nas_data/Pilatus1M/20190326Hopkins/cytc/buffer4/',
#     'buffer4',
#     '/nas_data/Pilatus1M/20190326Hopkins/reproc_0p015_dats/cytc/buffer4'
#     ],
#     ['/nas_data/Pilatus1M/20190326Hopkins/cytc/buffer5/',
#     'buffer5',
#     '/nas_data/Pilatus1M/20190326Hopkins/reproc_0p015_dats/cytc/buffer5'
#     ],
#     ['/nas_data/Pilatus1M/20190326Hopkins/cytc/buffer6/',
#     'buffer6',
#     '/nas_data/Pilatus1M/20190326Hopkins/reproc_0p015_dats/cytc/buffer6'
#     ],
#     ['/nas_data/Pilatus1M/20190326Hopkins/cytc/buffer7/',
#     'buffer7',
#     '/nas_data/Pilatus1M/20190326Hopkins/reproc_0p015_dats/cytc/buffer7'
#     ],
#     ['/nas_data/Pilatus1M/20190326Hopkins/cytc/buffer8/',
#     'buffer8',
#     '/nas_data/Pilatus1M/20190326Hopkins/reproc_0p015_dats/cytc/buffer8'
#     ],
#     ['/nas_data/Pilatus1M/20190326Hopkins/cytc/buffer9/',
#     'buffer9',
#     '/nas_data/Pilatus1M/20190326Hopkins/reproc_0p015_dats/cytc/buffer9'
#     ],
#     ['/nas_data/Pilatus1M/20190326Hopkins/cytc/buffer10/',
#     'buffer10',
#     '/nas_data/Pilatus1M/20190326Hopkins/reproc_0p015_dats/cytc/buffer10'
#     ],
#     ['/nas_data/Pilatus1M/20190326Hopkins/cytc/buffer11/',
#     'buffer11',
#     '/nas_data/Pilatus1M/20190326Hopkins/reproc_0p015_dats/cytc/buffer11'
#     ],
#     ['/nas_data/Pilatus1M/20190326Hopkins/cytc/native1/',
#     'native1',
#     '/nas_data/Pilatus1M/20190326Hopkins/reproc_0p015_dats/cytc/native1'
#     ],
#     ['/nas_data/Pilatus1M/20190326Hopkins/cytc/native2/',
#     'native2',
#     '/nas_data/Pilatus1M/20190326Hopkins/reproc_0p015_dats/cytc/native2'
#     ],
#     ['/nas_data/Pilatus1M/20190326Hopkins/cytc/native3/',
#     'native3',
#     '/nas_data/Pilatus1M/20190326Hopkins/reproc_0p015_dats/cytc/native3'
#     ],
# ]

# #March 2019
# cfg_file = '/nas_data/Pilatus1M/20190807Srinivas/SAXS_fullmask.cfg'

# # batch list should be a list of lists. Each entry should be as:
# # [source_dir, fprefix, output_dir]
# # Note that if fprefix is None, all files in the directory will be processed

# batch_list = [
#     # ['/nas_data/Pilatus1M/20190807Srinivas/cytc/native_buffer1/',
#     # 'native_buffer1',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/cytc/native_buffer1'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/cytc/native_cytc1/',
#     # 'native_cytc1',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/cytc/native_cytc1'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/cytc/buffer1/',
#     # 'buffer1',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/cytc/buffer1'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/cytc/cytc1/',
#     # 'cytc1',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/cytc/cytc1'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/cytc/buffer2/',
#     # 'buffer2',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/cytc/buffer2'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/cytc/cytc2/',
#     # 'cytc2',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/cytc/cytc2'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/cytc/cytc3/',
#     # 'cytc3',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/cytc/cytc3'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/cytc/buffer3/',
#     # 'buffer3',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/cytc/buffer3'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/water/water7/',
#     # 'water7',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/water/water7'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/water/water8/',
#     # 'water8',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/water/water8'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/water/water9/',
#     # 'water9',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/water/water9'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/cytc/buffer4/',
#     # 'buffer4',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/cytc/buffer4'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/cytc/cytc4/',
#     # 'cytc4',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/cytc/cytc4'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/cytc/cytc5/',
#     # 'cytc5',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/cytc/cytc5'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/cytc/buffer5/',
#     # 'buffer5',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/cytc/buffer5'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/water/water15/',
#     # 'water15',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/water/water15'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/water/water16/',
#     # 'water16',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/water/water16'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/sosnick/buffer2/',
#     # 'buffer2',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/sosnick/buffer2'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/sosnick/ub1/',
#     # 'ub1',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/sosnick/ub1'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/sosnick/buffer3/',
#     # 'buffer3',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/sosnick/buffer3'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/sosnick/ub2/',
#     # 'ub2',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/sosnick/ub2'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/sosnick/ub3/',
#     # 'ub3',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/sosnick/ub3'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/sosnick/buffer4/',
#     # 'buffer4',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/sosnick/buffer4'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/sosnick/ub4/',
#     # 'ub4',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/sosnick/ub4'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/sosnick/buffer5/',
#     # 'buffer5',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/sosnick/buffer5'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/sosnick/buffer6/',
#     # 'buffer6',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/sosnick/buffer6'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/sosnick/ub5/',
#     # 'ub5',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/sosnick/ub5'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/sosnick/buffer7/',
#     # 'buffer7',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/sosnick/buffer7'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/sosnick/ub6/',
#     # 'ub6',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/sosnick/ub6'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/sosnick/ub7/',
#     # 'ub7',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/sosnick/ub7'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/sosnick/buffer8/',
#     # 'buffer8',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/sosnick/buffer8'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/sosnick/ub8/',
#     # 'ub8',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/sosnick/ub8'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/sosnick/ub9/',
#     # 'ub9',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/sosnick/ub9'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/sosnick/buffer9/',
#     # 'buffer9',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/sosnick/buffer9'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/sosnick/ub10/',
#     # 'ub10',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/sosnick/ub10'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/sosnick/ub11/',
#     # 'ub11',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/sosnick/ub11'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/sosnick/ub12/',
#     # 'ub12',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/sosnick/ub12'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/pinto/buffer1/',
#     # 'buffer1',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/pinto/buffer1'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/pinto/twt1/',
#     # 'twt1',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/pinto/twt1'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/pinto/tmt1/',
#     # 'tmt1',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/pinto/tmt1'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/pinto/tmt2/',
#     # 'tmt2',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/pinto/tmt2'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/pinto/twt2/',
#     # 'twt2',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/pinto/twt2'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/pinto/twt3/',
#     # 'twt3',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/pinto/twt3'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/pinto/tmt3/',
#     # 'tmt3',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/pinto/tmt3'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/pinto/buffer2/',
#     # 'buffer2',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/pinto/buffer2'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/martin/buffer3/',
#     # 'buffer3',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/martin/buffer3'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/martin/em1/',
#     # 'em1',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/martin/em1'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/martin/em2/',
#     # 'em2',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/martin/em2'
#     # ],
#     ['/nas_data/Pilatus1M/20190807Srinivas/martin/buffer1_PEG/',
#     'buffer1_PEG',
#     '/nas_data/Pilatus1M/20190807Srinivas/dats/martin/buffer1_PEG'
#     ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/martin/em1_PEG/',
#     # 'em1_PEG',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/martin/em1_PEG'
#     # ],
#     # ['/nas_data/Pilatus1M/20190807Srinivas/martin/em2_PEG/',
#     # 'em2_PEG',
#     # '/nas_data/Pilatus1M/20190807Srinivas/dats/martin/em2_PEG'
#     # ],
# ]

#December 2019
cfg_file = '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_SAXS.cfg'

# batch list should be a list of lists. Each entry should be as:
# [source_dir, fprefix, output_dir]
# Note that if fprefix is None, all files in the directory will be processed

batch_list = [
    # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc/cytc_01/',
    # 'cytc_01',
    # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/cytc/cytc_01'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc/cytc_02/',
    # 'cytc_02',
    # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/cytc/cytc_02'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc/buf_01/',
    # 'buf_01',
    # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/cytc/buf_01'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc/buf_02/',
    # 'buf_02',
    # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/cytc/buf_02'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc/buf_03/',
    # 'buf_03',
    # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/cytc/buf_03'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc/cytc_03/',
    # 'cytc_03',
    # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/cytc/cytc_03'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc/buf_04/',
    # 'buf_04',
    # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/cytc/buf_04'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc/cytc_04/',
    # 'cytc_04',
    # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/cytc/cytc_04'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc/buf_05/',
    # 'buf_05',
    # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/cytc/buf_05'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc/cytc_05/',
    # 'cytc_05',
    # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/cytc/cytc_05'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc/buf_06/',
    # 'buf_06',
    # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/cytc/buf_06'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc/buf_07/',
    # 'buf_07',
    # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/cytc/buf_07'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc/cytc_06/',
    # 'cytc_06',
    # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/cytc/cytc_06'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc_2/buf2_01/',
    # 'buf2_01',
    # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/cytc2/buf2_01'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc_2/cytc2_01/',
    # 'cytc2_01',
    # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/cytc2/cytc2_01'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc_2/buf2_02/',
    # 'buf2_02',
    # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/cytc2/buf2_02'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc_2/cytc2_02/',
    # 'cytc2_02',
    # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/cytc2/cytc2_02'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc_2/buf2_03/',
    # 'buf2_03',
    # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/cytc2/buf2_03'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/pinto_chaotic/buf_01/',
    # 'buf_01',
    # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/pinto_cf/buf_01'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/pinto_chaotic/twt_01/',
    # 'twt_01',
    # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/pinto_cf/twt_01'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/pinto_chaotic/buf_02/',
    # 'buf_02',
    # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/pinto_cf/buf_02'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/pinto_chaotic/twt_02/',
    # 'twt_02',
    # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/pinto_cf/twt_02'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/pinto_chaotic/buf_03/',
    # 'buf_03',
    # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/pinto_cf/buf_03'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/pinto_chaotic/twt_03/',
    # 'twt_03',
    # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/pinto_cf/twt_03'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/pinto_chaotic/buf_04/',
    # 'buf_04',
    # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/pinto_cf/buf_04'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/pinto_chaotic/twt_04/',
    # 'twt_04',
    # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/pinto_cf/twt_04'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/pinto_chaotic/buf_05/',
    # 'buf_05',
    # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/pinto_cf/buf_05'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_chaotic/buf_01/',
    # 'buf_01',
    # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/martin_cf/buf_01'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_chaotic/em_01/',
    # 'em_01',
    # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/martin_cf/em_01'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_chaotic/buf_02/',
    # 'buf_02',
    # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/martin_cf/buf_02'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_chaotic/em_02/',
    # 'em_02',
    # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/martin_cf/em_02'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_chaotic/buf_03/',
    # 'buf_03',
    # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/martin_cf/buf_03'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_chaotic/em_03/',
    # 'em_03',
    # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/martin_cf/em_03'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_chaotic/buf_04/',
    # 'buf_04',
    # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/martin_cf/buf_04'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_chaotic/em_04/',
    # 'em_04',
    # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/martin_cf/em_04'
    # ],
    ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_chaotic/buf_05/',
    'buf_05',
    '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/dats/martin_cf/buf_05'
    ],
]

ai, mask, q_range, maxlen, normlist, do_normalization, raw_settings, calibrate_dict, fliplr, flipud = saxs_raver.init_integration(cfg_file)

start_point = raw_settings.get('StartPoint')
end_point = raw_settings.get('EndPoint')


for source_dir, fprefix, output_dir in batch_list:
    print fprefix
    try:
        old_dir_list_dict = {}

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        diff_list, old_dir_list_dict = saxs_raver.getNewFiles(source_dir, old_dir_list_dict, fprefix)

        for name, stuff in diff_list:
            print name

            saxs_raver.doIntegration(output_dir, ai, mask, q_range,
                maxlen, normlist, do_normalization, calibrate_dict,
                start_point, end_point, fliplr, flipud,
                os.path.join(source_dir, name))

    except KeyboardInterrupt:
        break
