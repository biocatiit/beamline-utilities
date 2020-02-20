import os
import glob
import sys

os.sys.path.append(os.path.abspath('../pyfai_integration/'))
import saxs_raver

sys.path.append('/home/biocat/jbh_projects/bioxtasraw-git')
import bioxtasraw.RAWAPI as raw

#March 2019

# batch list should be a list of lists. Each entry should be as:
# [source_dir, fprefix, output_dir]
# Note that if fprefix is None, all files in the directory will be processed

# batch_list = [
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/cytc/native_buffer1/',
    # 'native_buffer1',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/cytc/native_buffer1'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/cytc/native_cytc1/',
    # 'native_cytc1',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/cytc/native_cytc1'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/cytc/buffer1/',
    # 'buffer1',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/cytc/buffer1'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/cytc/cytc1/',
    # 'cytc1',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/cytc/cytc1'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/cytc/buffer2/',
    # 'buffer2',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/cytc/buffer2'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/cytc/cytc2/',
    # 'cytc2',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/cytc/cytc2'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/cytc/cytc3/',
    # 'cytc3',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/cytc/cytc3'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/cytc/buffer3/',
    # 'buffer3',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/cytc/buffer3'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/water/water7/',
    # 'water7',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/water/water7'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/water/water8/',
    # 'water8',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/water/water8'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/water/water9/',
    # 'water9',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/water/water9'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/cytc/buffer4/',
    # 'buffer4',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/cytc/buffer4'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/cytc/cytc4/',
    # 'cytc4',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/cytc/cytc4'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/cytc/cytc5/',
    # 'cytc5',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/cytc/cytc5'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/cytc/buffer5/',
    # 'buffer5',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/cytc/buffer5'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/water/water15/',
    # 'water15',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/water/water15'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/water/water16/',
    # 'water16',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/water/water16'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/buffer2/',
    # 'buffer2',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/buffer2'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/ub1/',
    # 'ub1',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/ub1'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/buffer3/',
    # 'buffer3',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/buffer3'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/ub2/',
    # 'ub2',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/ub2'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/ub3/',
    # 'ub3',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/ub3'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/buffer4/',
    # 'buffer4',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/buffer4'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/ub4/',
    # 'ub4',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/ub4'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/buffer5/',
    # 'buffer5',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/buffer5'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/buffer6/',
    # 'buffer6',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/buffer6'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/ub5/',
    # 'ub5',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/ub5'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/buffer7/',
    # 'buffer7',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/buffer7'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/ub6/',
    # 'ub6',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/ub6'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/ub7/',
    # 'ub7',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/ub7'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/buffer8/',
    # 'buffer8',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/buffer8'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/ub8/',
    # 'ub8',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/ub8'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/ub9/',
    # 'ub9',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/ub9'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/buffer9/',
    # 'buffer9',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/buffer9'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/ub10/',
    # 'ub10',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/ub10'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/ub11/',
    # 'ub11',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/ub11'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick/ub12/',
    # 'ub12',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/sosnick/ub12'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/pinto/buffer1/',
    # 'buffer1',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/pinto/buffer1'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/pinto/twt1/',
    # 'twt1',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/pinto/twt1'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/pinto/tmt1/',
    # 'tmt1',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/pinto/tmt1'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/pinto/tmt2/',
    # 'tmt2',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/pinto/tmt2'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/pinto/twt2/',
    # 'twt2',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/pinto/twt2'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/pinto/twt3/',
    # 'twt3',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/pinto/twt3'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/pinto/tmt3/',
    # 'tmt3',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/pinto/tmt3'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/pinto/buffer2/',
    # 'buffer2',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/pinto/buffer2'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/martin/buffer3/',
    # 'buffer3',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/martin/buffer3'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/martin/em1/',
    # 'em1',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/martin/em1'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/martin/em2/',
    # 'em2',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/martin/em2'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/martin/buffer4/',
    # 'buffer4',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/martin/buffer4'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/martin/buffer1_PEG/',
    # 'buffer1_PEG',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/martin/buffer1_PEG'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/martin/em1_PEG/',
    # 'em1_PEG',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/martin/em1_PEG'
    # ],
    # ['/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/martin/em2_PEG/',
    # 'em2_PEG',
    # '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/dats/martin/em2_PEG'
    # ],
# ]

# # Dec 2019 chaotic flow
# batch_list = [
#     # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc/cytc_01/',
#     # 'cytc_01',
#     # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/cytc/cytc_01'
#     # ],
#     # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc/cytc_02/',
#     # 'cytc_02',
#     # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/cytc/cytc_02'
#     # ],
#     # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc/buf_01/',
#     # 'buf_01',
#     # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/cytc/buf_01'
#     # ],
#     # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc/buf_02/',
#     # 'buf_02',
#     # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/cytc/buf_02'
#     # ],
#     # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc/buf_03/',
#     # 'buf_03',
#     # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/cytc/buf_03'
#     # ],
#     # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc/cytc_03/',
#     # 'cytc_03',
#     # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/cytc/cytc_03'
#     # ],
#     # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc/buf_04/',
#     # 'buf_04',
#     # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/cytc/buf_04'
#     # ],
#     # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc/cytc_04/',
#     # 'cytc_04',
#     # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/cytc/cytc_04'
#     # ],
#     # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc/buf_05/',
#     # 'buf_05',
#     # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/cytc/buf_05'
#     # ],
#     # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc/cytc_05/',
#     # 'cytc_05',
#     # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/cytc/cytc_05'
#     # ],
#     # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc/buf_06/',
#     # 'buf_06',
#     # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/cytc/buf_06'
#     # ],
#     # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc/buf_07/',
#     # 'buf_07',
#     # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/cytc/buf_07'
#     # ],
#     # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc/cytc_06/',
#     # 'cytc_06',
#     # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/cytc/cytc_06'
#     # ],
#     ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc_2/buf2_01/',
#     'buf2_01',
#     '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/cytc2/buf2_01'
#     ],
#     ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc_2/cytc2_01/',
#     'cytc2_01',
#     '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/cytc2/cytc2_01'
#     ],
#     ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc_2/buf2_02/',
#     'buf2_02',
#     '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/cytc2/buf2_02'
#     ],
#     ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc_2/cytc2_02/',
#     'cytc2_02',
#     '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/cytc2/cytc2_02'
#     ],
#     ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc_2/buf2_03/',
#     'buf2_03',
#     '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/cytc2/buf2_03'
#     ],
#     ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/pinto_chaotic/buf_01/',
#     'buf_01',
#     '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/pinto_cf/buf_01'
#     ],
#     ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/pinto_chaotic/twt_01/',
#     'twt_01',
#     '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/pinto_cf/twt_01'
#     ],
#     ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/pinto_chaotic/buf_02/',
#     'buf_02',
#     '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/pinto_cf/buf_02'
#     ],
#     ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/pinto_chaotic/twt_02/',
#     'twt_02',
#     '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/pinto_cf/twt_02'
#     ],
#     ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/pinto_chaotic/buf_03/',
#     'buf_03',
#     '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/pinto_cf/buf_03'
#     ],
#     ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/pinto_chaotic/twt_03/',
#     'twt_03',
#     '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/pinto_cf/twt_03'
#     ],
#     ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/pinto_chaotic/buf_04/',
#     'buf_04',
#     '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/pinto_cf/buf_04'
#     ],
#     ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/pinto_chaotic/twt_04/',
#     'twt_04',
#     '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/pinto_cf/twt_04'
#     ],
#     ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/pinto_chaotic/buf_05/',
#     'buf_05',
#     '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/pinto_cf/buf_05'
#     ],
#     ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_chaotic/buf_01/',
#     'buf_01',
#     '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/martin_cf/buf_01'
#     ],
#     ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_chaotic/em_01/',
#     'em_01',
#     '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/martin_cf/em_01'
#     ],
#     ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_chaotic/buf_02/',
#     'buf_02',
#     '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/martin_cf/buf_02'
#     ],
#     ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_chaotic/em_02/',
#     'em_02',
#     '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/martin_cf/em_02'
#     ],
#     ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_chaotic/buf_03/',
#     'buf_03',
#     '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/martin_cf/buf_03'
#     ],
#     ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_chaotic/em_03/',
#     'em_03',
#     '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/martin_cf/em_03'
#     ],
#     ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_chaotic/buf_04/',
#     'buf_04',
#     '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/martin_cf/buf_04'
#     ],
#     ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_chaotic/em_04/',
#     'em_04',
#     '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/martin_cf/em_04'
#     ],
#     ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_chaotic/buf_05/',
#     'buf_05',
#     '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/dats/martin_cf/buf_05'
#     ],
# ]

# Dec 2019 laminar flow
batch_list = [
    ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_laminar/em01/',
    'em01',
    '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/martin_lf/em01'
    ],
    ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_laminar/em02/',
    'em02',
    '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/martin_lf/em02'
    ],
    ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_laminar/em03/',
    'em03',
    '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/martin_lf/em03'
    ],
    ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_laminar/em04/',
    'em04',
    '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/martin_lf/em04'
    ],
    ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_laminar/em05/',
    'em05',
    '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/martin_lf/em05'
    ],
    ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_laminar/em06/',
    'em06',
    '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/martin_lf/em06'
    ],
    ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_laminar/em07/',
    'em07',
    '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/martin_lf/em07'
    ],
    ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_laminar/em08/',
    'em08',
    '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/martin_lf/em08'
    ],
    ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_laminar/em09/',
    'em09',
    '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/martin_lf/em09'
    ],
    ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_laminar/em10/',
    'em10',
    '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/martin_lf/em10'
    ],
]

# base_config_dir = '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing'
# base_config_dir = '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing'
base_config_dir = '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/masks'

# ai, mask, q_range, maxlen, normlist, do_normalization, raw_settings, calibrate_dict, fliplr, flipud = saxs_raver.init_integration(cfg_file)

# start_point = raw_settings.get('StartPoint')
# end_point = raw_settings.get('EndPoint')


for source_dir, fprefix, output_dir in batch_list:
    print fprefix

    try:
        old_dir_list_dict = {}

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        print 'Getting file list'
        diff_list, old_dir_list_dict = saxs_raver.getNewFiles(source_dir, old_dir_list_dict, fprefix)

        print 'Loading config files'
        # Chaotic flow
        # f_list = glob.glob(os.path.join(source_dir, '{}_*_0001_*.tif'.format(fprefix)))
        # fnum_list = [int(fname.split('_')[-1].strip('.tif')) for fname in f_list]
        # fnum_list.sort()

        # Laminar flow
        f_list = glob.glob(os.path.join(source_dir, '{}_???_s???_0001_*.tif'.format(fprefix)))
        fnum_list = list(set([int(fname.split('_')[-1].strip('.tif')) for fname in f_list]))
        fnum_list.sort()
        step_list = list(set([fname.split('_')[-3] for fname in f_list]))
        step_list.sort()

        config_dict = {}

        # Chaotic flow August 2019 and December 2019
        # if 'martin' in source_dir:
        #     gen_config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_martin_basic.cfg'))
        #     for fnum in fnum_list:
        #         if os.path.exists(os.path.join(base_config_dir, 'SAXS_martin_{:03d}.cfg'.format(fnum))):
        #             config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_martin_{:03d}.cfg'.format(fnum)))
        #         else:
        #             config_results = gen_config_results

        #         config_dict[fnum] = config_results

        # elif 'pinto' in source_dir:
        #     gen_config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_pinto_basic.cfg'))
        #     for fnum in fnum_list:
        #         if os.path.exists(os.path.join(base_config_dir, 'SAXS_pinto_{:03d}.cfg'.format(fnum))):
        #             config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_pinto_{:03d}.cfg'.format(fnum)))
        #         else:
        #             config_results = gen_config_results

        #         config_dict[fnum] = config_results

        # elif 'sosnick' in source_dir:
        #     if len(fnum_list) == 30:
        #         prefix='short'
        #     else:
        #         prefix='long'

        #     gen_config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_sosnick_{}_basic.cfg'.format(prefix)))
        #     for fnum in fnum_list:
        #         if os.path.exists(os.path.join(base_config_dir, 'SAXS_sosnick_{}_{:03d}.cfg'.format(prefix, fnum))):
        #             config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_sosnick_{}_{:03d}.cfg'.format(prefix, fnum)))
        #         else:
        #             config_results = gen_config_results

        #         config_dict[fnum] = config_results

        # elif 'cytc' in source_dir:
        #     # if fprefix in ['native_cytc1', 'native_buffer1']:
        #     #     prefix = 'native'
        #     # elif fprefix in ['buffer2', 'buffer3', 'cytc2', 'cytc3']:
        #     #     prefix = '0808'
        #     # elif fprefix in ['buffer4' , 'buffer5', 'cytc4', 'cytc5']:
        #     #     prefix = '0809'

        #     # gen_config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_cytc_{}_basic.cfg'.format(prefix)))

        #     # for fnum in fnum_list:
        #     #     if os.path.exists(os.path.join(base_config_dir, 'SAXS_cytc_{}_{:03d}.cfg'.format(prefix, fnum))):
        #     #         config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_cytc_{}_{:03d}.cfg'.format(prefix, fnum)))
        #     #     else:
        #     #         config_results = gen_config_results

        #     #     config_dict[fnum] = config_results

        #     gen_config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_cytc_basic.cfg'))
        #     for fnum in fnum_list:
        #         if os.path.exists(os.path.join(base_config_dir, 'SAXS_cytc_{:03d}.cfg'.format(fnum))):
        #             config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_cytc_{:03d}.cfg'.format(fnum)))
        #         else:
        #             config_results = gen_config_results

        #         config_dict[fnum] = config_results


        # December 2019
        if 'martin' in source_dir:
            for fnum in fnum_list:
                print fnum
                # gen_config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'em_basic_{:04d}.cfg'.format(fnum)))
                gen_config_results = raw.load_settings(os.path.join(base_config_dir, 'em_basic_{:04d}.cfg'.format(fnum)))
                for step in step_list:
                    print step
                    if os.path.exists(os.path.join(base_config_dir, 'em_{}_{:04d}.cfg'.format(step, fnum))):
                        # print os.path.join(base_config_dir, 'em_{}_{:04d}.cfg'.format(step, fnum))
                        # config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'em_{}_{:04d}.cfg'.format(step, fnum)))
                        config_results = raw.load_settings(os.path.join(base_config_dir, 'em_{}_{:04d}.cfg'.format(step, fnum)))
                    else:
                        # print 'basic'
                        config_results = gen_config_results

                    config_dict[(fnum, step)] = config_results

        print 'Processing images'
        for name, stuff in diff_list:
            print name

            fnum = int(name.split('_')[-1].strip('.tif'))
            step = name.split('_')[-3]
            # ai, mask, q_range, maxlen, normlist, do_normalization, raw_settings, calibrate_dict, fliplr, flipud = config_dict[(fnum, step)]
            raw_settings = config_dict[(fnum, step)]
            # start_point = raw_settings.get('StartPoint')
            # end_point = raw_settings.get('EndPoint')

            # saxs_raver.doIntegration(output_dir, ai, mask, q_range,
            #     maxlen, normlist, do_normalization, calibrate_dict,
            #     start_point, end_point, fliplr, flipud,
            #     os.path.join(source_dir, name))

            dats, _ = raw.load_and_integrate_images([os.path.join(source_dir,name)], raw_settings)

            data = dats[0]

            raw.save_dat(data, raw_settings, datadir=output_dir)

    except KeyboardInterrupt:
        break
