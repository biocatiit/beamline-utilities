import os
import glob
import sys
import time

# os.sys.path.append('/Users/jessehopkins/Desktop/temp/bioxtasraw-git')
# os.sys.path.append(os.path.abspath('../pyfai_integration/'))
# import saxs_raver

# sys.path.append('/home/biocat/jbh_projects/bioxtasraw-git')

import bioxtasraw.RAWAPI as raw

def getNewFiles(target_dir, old_dir_list_dict, fprefix, extra_name, img_ext):
    # print 'Getting New Files'
    dir_list = os.listdir(target_dir)

    dir_list_dict = {}

    for each_file in dir_list:
        if os.path.splitext(each_file)[1].lstrip('.') == img_ext and extra_name in os.path.split(each_file)[1]:
            if fprefix is None or each_file.startswith(fprefix):
                try:
                    full_path = os.path.join(target_dir, each_file)
                    dir_list_dict[each_file] = (os.path.getmtime(full_path),
                        os.path.getsize(full_path))
                except OSError:
                    pass

    diff_list = list(set(dir_list_dict.items()) - set(old_dir_list_dict.items()))
    diff_list.sort(key = lambda name: name[0])

    old_dir_list_dict.update(diff_list)

    return diff_list, old_dir_list_dict

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

# # Dec 2019 laminar flow
# batch_list = [
#     # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_laminar/em01/',
#     # 'em01',
#     # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/martin_lf/em01'
#     # ],
#     # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_laminar/em02/',
#     # 'em02',
#     # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/martin_lf/em02'
#     # ],
#     # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_laminar/em03/',
#     # 'em03',
#     # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/martin_lf/em03'
#     # ],
#     # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_laminar/em04/',
#     # 'em04',
#     # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/martin_lf/em04'
#     # ],
#     # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_laminar/em05/',
#     # 'em05',
#     # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/martin_lf/em05'
#     # ],
#     # ['/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/martin_laminar/em06/',
#     # 'em06',
#     # '/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/martin_lf/em06'
#     # ],
#     # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_laminar/em07/',
#     # 'em07',
#     # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/martin_lf/em07'
#     # ],
#     # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_laminar/em08/',
#     # 'em08',
#     # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/martin_lf/em08'
#     # ],
#     # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_laminar/em09/',
#     # 'em09',
#     # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/martin_lf/em09'
#     # ],
#     # ['/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_laminar/em10/',
#     # 'em10',
#     # '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/martin_lf/em10'
#     # ],
#     # ['/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/2019_1210Pinto/mt_01',
#     # 'mt_01',
#     # '/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/pinto_lf/mt_01'
#     # ],
#     # ['/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/2019_1210Pinto/mt_02',
#     # 'mt_02',
#     # '/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/pinto_lf/mt_02'
#     # ],
#     # ['/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/2019_1210Pinto/mt_03',
#     # 'mt_03',
#     # '/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/pinto_lf/mt_03'
#     # ],
#     # ['/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/2019_1210Pinto/wt_01',
#     # 'wt_01',
#     # '/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/pinto_lf/wt_01'
#     # ],
#     # ['/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/2019_1210Pinto/wt_02',
#     # 'wt_02',
#     # '/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/pinto_lf/wt_02'
#     # ],
#     # ['/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/2019_1210Pinto/wt_03',
#     # 'wt_03',
#     # '/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/pinto_lf/wt_03'
#     # ],
#     # ['/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/2019_1210Pinto/wt_eq_01',
#     # 'wt_eq_01',
#     # '/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/pinto_lf/wt_eq_01'
#     # ],
#     # ['/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/2019_1210Pinto/wt_eq_02',
#     # 'wt_eq_02',
#     # '/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/pinto_lf/wt_eq_02'
#     # ],
#     # ['/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/na/ric_mgs_01',
#     # 'ric_mgs_01',
#     # '/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/na_lf/ric_mgs_01'
#     # ],
#     # ['/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/na/ric_01',
#     # 'ric_01',
#     # '/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/na_lf/ric_01'
#     # ],
#     # ['/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/na/ric452_mgs_01',
#     # 'ric452_mgs_01',
#     # '/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/na_lf/ric452_mgs_01'
#     # ],
#     # ['/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/na/buf_01',
#     # 'buf_01',
#     # '/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/na_lf/buf_01'
#     # ],
#     # ['/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/na/ric452_mgs_02',
#     # 'ric452_mgs_02',
#     # '/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/na_lf/ric452_mgs_02'
#     # ],
#     # ['/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/na/ric452_mgs_03',
#     # 'ric452_mgs_03',
#     # '/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/na_lf/ric452_mgs_03'
#     # ],
#     # ['/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/na/ric452_01',
#     # 'ric452_01',
#     # '/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/na_lf/ric452_01'
#     # ],
#     # ['/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/na/ric_mgo_01',
#     # 'ric_mgo_01',
#     # '/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/na_lf/ric_mgo_01'
#     # ],
#     ['/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/na/ric_mgo_02',
#     'ric_mgo_02',
#     '/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/na_lf/ric_mgo_02'
#     ],
#     ['/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/na/buf_02',
#     'buf_02',
#     '/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/na_lf/buf_02'
#     ],
#     ['/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/na/ric452_mgo_01',
#     'ric452_mgo_01',
#     '/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/na_lf/ric452_mgo_01'
#     ],
#     ['/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/na/buf_03',
#     'buf_03',
#     '/Volumes/detectors_vol1/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/dats/na_lf/buf_03'
#     ],
# ]

# batch_list = [
    # ['/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/RM01',
    # 'RM01',
    # '/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/processing/profiles/RM01'
    # ],
    # ['/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/RM02',
    # 'RM02',
    # '/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/processing/profiles/RM02'
    # ],
    # ['/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/RM03',
    # 'RM03',
    # '/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/processing/profiles/RM03'
    # ],
    # ['/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/RM04',
    # 'RM04',
    # '/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/processing/profiles/RM04'
    # ],
    # ['/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/RM05',
    # 'RM05',
    # '/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/processing/profiles/RM05'
    # ],
    # ['/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/RM06',
    # 'RM06',
    # '/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/processing/profiles/RM06'
    # ],
    # ['/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/RM08',
    # 'RM08',
    # '/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/processing/profiles/RM08'
    # ],
    # ['/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/RM09',
    # 'RM09',
    # '/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/processing/profiles/RM09'
    # ],
    # ['/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/RM10',
    # 'RM10',
    # '/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/processing/profiles/RM10'
    # ],
    # ['/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/RM12',
    # 'RM12',
    # '/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/processing/profiles/RM12'
    # ],
    # ['/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/RM13',
    # 'RM13',
    # '/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/processing/profiles/RM13'
    # ],
    # ['/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/RM15',
    # 'RM15',
    # '/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/processing/profiles/RM15'
    # ],
    # ['/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/RM16',
    # 'RM16',
    # '/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/processing/profiles/RM16'
    # ],
    # ['/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/RM17',
    # 'RM17',
    # '/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/processing/profiles/RM17'
    # ],
    # ['/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/RM18',
    # 'RM18',
    # '/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/processing/profiles/RM18'
    # ],
    # ['/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/RM19',
    # 'RM19',
    # '/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/processing/profiles/RM19'
    # ],
    # ['/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/RM20',
    # 'RM20',
    # '/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/processing/profiles/RM20'
    # ],
    # ['/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/RM21',
    # 'RM21',
    # '/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/processing/profiles/RM21'
    # ],
    # ['/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/RM22',
    # 'RM22',
    # '/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/processing/profiles/RM22'
    # ],
    # ]


# # April 2022, Bilsel long scans
# batch_list = [
#     ['/nas_data/Eiger2xe9M/2022_Run1/20220423_Bilsel/OB05',
#     'OB05',
#     '/nas_data/Eiger2xe9M/2022_Run1/20220423_Bilsel/processing/profiles/OB05'
#     ],
#     # ['/nas_data/Eiger2xe9M/2022_Run1/20220423_Bilsel/OB06',
#     # 'OB06',
#     # '/nas_data/Eiger2xe9M/2022_Run1/20220423_Bilsel/processing/profiles/OB06'
#     # ],
#     # ['/nas_data/Eiger2xe9M/2022_Run1/20220423_Bilsel/OB07',
#     # 'OB07',
#     # '/nas_data/Eiger2xe9M/2022_Run1/20220423_Bilsel/processing/profiles/OB07'
#     # ],
#     # ['/nas_data/Eiger2xe9M/2022_Run1/20220423_Bilsel/OB08',
#     # 'OB08',
#     # '/nas_data/Eiger2xe9M/2022_Run1/20220423_Bilsel/processing/profiles/OB08'
#     # ],
#     # ['/nas_data/Eiger2xe9M/2022_Run1/20220423_Bilsel/OB09',
#     # 'OB09',
#     # '/nas_data/Eiger2xe9M/2022_Run1/20220423_Bilsel/processing/profiles/OB09'
#     # ],
#     # ['/nas_data/Eiger2xe9M/2022_Run1/20220423_Bilsel/OB10',
#     # 'OB10',
#     # '/nas_data/Eiger2xe9M/2022_Run1/20220423_Bilsel/processing/profiles/OB10'
#     # ],
#     # ['/nas_data/Eiger2xe9M/2022_Run1/20220423_Bilsel/OB11',
#     # 'OB11',
#     # '/nas_data/Eiger2xe9M/2022_Run1/20220423_Bilsel/processing/profiles/OB11'
#     # ],
#     # ['/nas_data/Eiger2xe9M/2022_Run1/20220423_Bilsel/OB12',
#     # 'OB12',
#     # '/nas_data/Eiger2xe9M/2022_Run1/20220423_Bilsel/processing/profiles/OB12'
#     # ],
#     ]

# # April 2022, Bilsel short scans
# batch_list = [
#     ['/nas_data/Eiger2xe9M/2022_Run1/20220423_Bilsel/OB03',
#     'OB03',
#     '/nas_data/Eiger2xe9M/2022_Run1/20220423_Bilsel/processing/profiles/OB03'
#     ],
#     ['/nas_data/Eiger2xe9M/2022_Run1/20220423_Bilsel/OB04',
#     'OB04',
#     '/nas_data/Eiger2xe9M/2022_Run1/20220423_Bilsel/processing/profiles/OB04'
#     ],
#     ]

# # April 2022, Cytochrome C
# batch_list = [
#     # ['/nas_data/Eiger2xe9M/2022_Run1/20220420_Hopkins/cytc/refolding/cytc_01',
#     # 'cytc_01',
#     # '/nas_data/Eiger2xe9M/2022_Run1/20220420_Hopkins/processing/profiles/cytc/refolding/cytc_01'
#     # ],
#     # ['/nas_data/Eiger2xe9M/2022_Run1/20220420_Hopkins/cytc/refolding/cytc_02',
#     # 'cytc_02',
#     # '/nas_data/Eiger2xe9M/2022_Run1/20220420_Hopkins/processing/profiles/cytc/refolding/cytc_02'
#     # ],
#     # ['/nas_data/Eiger2xe9M/2022_Run1/20220420_Hopkins/cytc/refolding/cytc_03',
#     # 'cytc_03',
#     # '/nas_data/Eiger2xe9M/2022_Run1/20220420_Hopkins/processing/profiles/cytc/refolding/cytc_03'
#     # ],
#     # ['/nas_data/Eiger2xe9M/2022_Run1/20220420_Hopkins/cytc/refolding/cytc_04',
#     # 'cytc_04',
#     # '/nas_data/Eiger2xe9M/2022_Run1/20220420_Hopkins/processing/profiles/cytc/refolding/cytc_04'
#     # ],
#     ['/nas_data/Eiger2xe9M/2022_Run1/20220420_Hopkins/cytc/refolding/cytc_05',
#     'cytc_05',
#     '/nas_data/Eiger2xe9M/2022_Run1/20220420_Hopkins/processing/profiles/cytc/refolding/cytc_05'
#     ],
#     # ['/nas_data/Eiger2xe9M/2022_Run1/20220420_Hopkins/cytc/refolding/cytc_06',
#     # 'cytc_06',
#     # '/nas_data/Eiger2xe9M/2022_Run1/20220420_Hopkins/processing/profiles/cytc/refolding/cytc_06'
#     # ],
#     ]


# base_config_dir = '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing'
# base_config_dir = '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing'
# base_config_dir = '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/masks'
# base_config_dir = '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/masks'
# base_config_dir = '/nas_data/Eiger2xe9M/2022_Run1/20220423_Bilsel/processing/masks/full'
# base_config_dir = '/nas_data/Eiger2xe9M/2022_Run1/20220423_Bilsel/processing/masks/short'
# base_config_dir = '/nas_data/Eiger2xe9M/2022_Run1/20220420_Hopkins/processing/masks/cytc/refolding'

#New batch definition:
#[
#images dir,
#images prefix,
#profiles output dir,
#mask dir,
#mask prefix
#]

# April 2023, Pollack

batch_list = [
    ['/nas_data/Eiger2x/2023_Run1/20230405_Pollack/LP01/images',
    'LP01',
    '/nas_data/SAXS/2023_Run1/20230405_Pollack/LP01/profiles',
    '/nas_data/Eiger2x/2023_Run1/20230405_Pollack/processing/masks/day1',
    'LP'
    ],
    ['/nas_data/Eiger2x/2023_Run1/20230405_Pollack/LP02/images',
    'LP02',
    '/nas_data/SAXS/2023_Run1/20230405_Pollack/LP02/profiles',
    '/nas_data/Eiger2x/2023_Run1/20230405_Pollack/processing/masks/day1',
    'LP'
    ],
    ['/nas_data/Eiger2x/2023_Run1/20230405_Pollack/LP03/images',
    'LP03',
    '/nas_data/SAXS/2023_Run1/20230405_Pollack/LP03/profiles',
    '/nas_data/Eiger2x/2023_Run1/20230405_Pollack/processing/masks/day1',
    'LP'
    ],
    ['/nas_data/Eiger2x/2023_Run1/20230405_Pollack/LP04/images',
    'LP04',
    '/nas_data/SAXS/2023_Run1/20230405_Pollack/LP04/profiles',
    '/nas_data/Eiger2x/2023_Run1/20230405_Pollack/processing/masks/day1',
    'LP'
    ],
    ['/nas_data/Eiger2x/2023_Run1/20230405_Pollack/LP05/images/renum',
    'LP05',
    '/nas_data/SAXS/2023_Run1/20230405_Pollack/LP05/profiles',
    '/nas_data/Eiger2x/2023_Run1/20230405_Pollack/processing/masks/day1',
    'LP'
    ],
    ['/nas_data/Eiger2x/2023_Run1/20230405_Pollack/LP06/images/renum',
    'LP06',
    '/nas_data/SAXS/2023_Run1/20230405_Pollack/LP06/profiles',
    '/nas_data/Eiger2x/2023_Run1/20230405_Pollack/processing/masks/day1',
    'LP'
    ],
    ['/nas_data/Eiger2x/2023_Run1/20230405_Pollack/LP07/images',
    'LP07',
    '/nas_data/SAXS/2023_Run1/20230405_Pollack/LP07/profiles',
    '/nas_data/Eiger2x/2023_Run1/20230405_Pollack/processing/masks/day2',
    'LP'
    ],
    ['/nas_data/Eiger2x/2023_Run1/20230405_Pollack/LP08/images',
    'LP08',
    '/nas_data/SAXS/2023_Run1/20230405_Pollack/LP08/profiles',
    '/nas_data/Eiger2x/2023_Run1/20230405_Pollack/processing/masks/day2',
    'LP'
    ],
    ['/nas_data/Eiger2x/2023_Run1/20230405_Pollack/LP09/images',
    'LP09',
    '/nas_data/SAXS/2023_Run1/20230405_Pollack/LP09/profiles',
    '/nas_data/Eiger2x/2023_Run1/20230405_Pollack/processing/masks/day2',
    'LP'
    ],
    ['/nas_data/Eiger2x/2023_Run1/20230405_Pollack/LP10/images',
    'LP10',
    '/nas_data/SAXS/2023_Run1/20230405_Pollack/LP10/profiles',
    '/nas_data/Eiger2x/2023_Run1/20230405_Pollack/processing/masks/day3',
    'LP'
    ],
    ['/nas_data/Eiger2x/2023_Run1/20230405_Pollack/LP11/images',
    'LP11',
    '/nas_data/SAXS/2023_Run1/20230405_Pollack/LP11/profiles',
    '/nas_data/Eiger2x/2023_Run1/20230405_Pollack/processing/masks/day3',
    'LP'
    ],
    ['/nas_data/Eiger2x/2023_Run1/20230405_Pollack/LP12/images',
    'LP12',
    '/nas_data/SAXS/2023_Run1/20230405_Pollack/LP12/profiles',
    '/nas_data/Eiger2x/2023_Run1/20230405_Pollack/processing/masks/day3',
    'LP'
    ],
    ['/nas_data/Eiger2x/2023_Run1/20230405_Pollack/LP13/images',
    'LP13',
    '/nas_data/SAXS/2023_Run1/20230405_Pollack/LP13/profiles',
    '/nas_data/Eiger2x/2023_Run1/20230405_Pollack/processing/masks/day3',
    'LP'
    ],
    ['/nas_data/Eiger2x/2023_Run1/20230405_Pollack/LP14/images',
    'LP14',
    '/nas_data/SAXS/2023_Run1/20230405_Pollack/LP14/profiles',
    '/nas_data/Eiger2x/2023_Run1/20230405_Pollack/processing/masks/day3',
    'LP'
    ],
    ['/nas_data/Eiger2x/2023_Run1/20230405_Pollack/LP15/images',
    'LP15',
    '/nas_data/SAXS/2023_Run1/20230405_Pollack/LP15/profiles',
    '/nas_data/Eiger2x/2023_Run1/20230405_Pollack/processing/masks/day3',
    'LP'
    ],
    ['/nas_data/Eiger2x/2023_Run1/20230409_Gupta/KG03/images',
    'KG03',
    '/nas_data/SAXS/2023_Run1/20230409_Gupta/KG03/profiles',
    '/nas_data/Eiger2x/2023_Run1/20230409_Gupta/processing/masks',
    'KG'
    ],
    # ['/nas_data/Eiger2x/2023_Run1/20230409_Gupta/KG04/images',
    # 'KG04',
    # '/nas_data/SAXS/2023_Run1/20230409_Gupta/KG04/profiles',
    # '/nas_data/Eiger2x/2023_Run1/20230409_Gupta/processing/masks',
    # 'KG'
    # ],
    # ['/nas_data/Eiger2x/2023_Run1/20230409_Gupta/KG05/images',
    # 'KG05',
    # '/nas_data/SAXS/2023_Run1/20230409_Gupta/KG05/profiles',
    # '/nas_data/Eiger2x/2023_Run1/20230409_Gupta/processing/masks',
    # 'KG'
    # ],
    # ['/nas_data/Eiger2x/2023_Run1/20230409_Gupta/KG06/images',
    # 'KG06',
    # '/nas_data/SAXS/2023_Run1/20230409_Gupta/KG06/profiles',
    # '/nas_data/Eiger2x/2023_Run1/20230409_Gupta/processing/masks',
    # 'KG'
    # ],
    # ['/nas_data/Eiger2x/2023_Run1/20230409_Gupta/KG07/images',
    # 'KG07',
    # '/nas_data/SAXS/2023_Run1/20230409_Gupta/KG07/profiles',
    # '/nas_data/Eiger2x/2023_Run1/20230409_Gupta/processing/masks',
    # 'KG'
    # ],
    # ['/nas_data/Eiger2x/2023_Run1/20230409_Gupta/KG08/images',
    # 'KG08',
    # '/nas_data/SAXS/2023_Run1/20230409_Gupta/KG08/profiles',
    # '/nas_data/Eiger2x/2023_Run1/20230409_Gupta/processing/masks',
    # 'KG'
    # ],
    # ['/nas_data/Eiger2x/2023_Run1/20230409_Gupta/KG09/images',
    # 'KG09',
    # '/nas_data/SAXS/2023_Run1/20230409_Gupta/KG09/profiles',
    # '/nas_data/Eiger2x/2023_Run1/20230409_Gupta/processing/masks',
    # 'KG'
    # ],
    # ['/nas_data/Eiger2x/2023_Run1/20230409_Gupta/KG10/images',
    # 'KG10',
    # '/nas_data/SAXS/2023_Run1/20230409_Gupta/KG10/profiles',
    # '/nas_data/Eiger2x/2023_Run1/20230409_Gupta/processing/masks',
    # 'KG'
    # ],
    # ['/nas_data/Eiger2x/2023_Run1/20230409_Gupta/KG11/images',
    # 'KG11',
    # '/nas_data/SAXS/2023_Run1/20230409_Gupta/KG11/profiles',
    # '/nas_data/Eiger2x/2023_Run1/20230409_Gupta/processing/masks',
    # 'KG'
    # ],
    # ['/nas_data/Eiger2x/2023_Run1/20230409_Gupta/KG12/images',
    # 'KG12',
    # '/nas_data/SAXS/2023_Run1/20230409_Gupta/KG12/profiles',
    # '/nas_data/Eiger2x/2023_Run1/20230409_Gupta/processing/masks',
    # 'KG'
    # ],
    ]

#Pilatus
# img_ext = 'tif'
# zpad = 4
# extra_name = ''

#Eiger
img_ext = 'h5'
zpad = 6
extra_name = 'data'


for source_dir, fprefix, output_dir, mask_dir, mask_prefix in batch_list:
    print(fprefix)

    try:
        old_dir_list_dict = {}

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        print('Getting file list')
        diff_list, old_dir_list_dict = getNewFiles(source_dir, old_dir_list_dict, fprefix, extra_name, img_ext)
        
        # Chaotic flow
        f_list = glob.glob(os.path.join(source_dir, '{}_*_0001_{}*.{}'.format(fprefix, extra_name, img_ext)))
        fnum_list = list(set([int(fname.split('_')[-1].rstrip('{}'.format(img_ext)).rstrip('.')) for fname in f_list]))
        fnum_list.sort()

        print('Processing images')

        gen_config_results = raw.load_settings(os.path.join(mask_dir, '{}_basic.cfg'.format(mask_prefix)))

        for fnum in fnum_list:
            print(fnum)
            print('Loading config file')
            if os.path.exists(os.path.join(mask_dir, '{}_{:04d}.cfg'.format(mask_prefix, fnum))):
                raw_settings = raw.load_settings(os.path.join(mask_dir, '{}_{:04d}.cfg'.format(mask_prefix, fnum)))
                # print('point config')
            else:
                raw_settings = gen_config_results
                # print('generic config')

            
            for name, stuff in diff_list:

                file_fnum = int(os.path.splitext(name)[0].split('_')[-1])

                if file_fnum == fnum:
                    print(name)

                    dats, _ = raw.load_and_integrate_images([os.path.join(source_dir,name)], raw_settings)
                    data = dats[0]

                    raw.save_profile(data, settings=raw_settings, datadir=output_dir)

            if raw_settings != gen_config_results:
                del raw_settings

    except KeyboardInterrupt:
        break

    # try:
    #     old_dir_list_dict = {}

    #     if not os.path.exists(output_dir):
    #         os.makedirs(output_dir)

    #     print('Getting file list')
    #     diff_list, old_dir_list_dict = getNewFiles(source_dir, old_dir_list_dict, fprefix, extra_name, img_ext)
    #     print('Loading config files')
    #     # Chaotic flow
    #     f_list = glob.glob(os.path.join(source_dir, '{}_*_0001_{}*.{}'.format(fprefix, extra_name, img_ext)))
    #     fnum_list = list(set([int(fname.split('_')[-1].rstrip('{}'.format(img_ext)).rstrip('.')) for fname in f_list]))
    #     fnum_list.sort()

    #     # print(fnum_list)

    #     # # Laminar flow
    #     # # f_list = glob.glob(os.path.join(source_dir, '{}_???_s???_0001_*.tif'.format(fprefix)))
    #     # f_list = glob.glob(os.path.join(source_dir, '{}_???_s???_0001_*.tif'.format(fprefix)))
    #     # if len(f_list) == 0:
    #     #     f_list = glob.glob(os.path.join(source_dir, '{}_???_s????_0001_*.tif'.format(fprefix)))
    #     # fnum_list = list(set([int(fname.split('_')[-1].strip('.tif')) for fname in f_list]))
    #     # fnum_list.sort()
    #     # step_list = list(set([fname.split('_')[-3] for fname in f_list]))
    #     # step_list.sort()

    #     config_dict = {}

    #     # Chaotic flow August 2019 and December 2019
    #     # if 'martin' in source_dir:
    #     #     gen_config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_martin_basic.cfg'))
    #     #     for fnum in fnum_list:
    #     #         if os.path.exists(os.path.join(base_config_dir, 'SAXS_martin_{:03d}.cfg'.format(fnum))):
    #     #             config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_martin_{:03d}.cfg'.format(fnum)))
    #     #         else:
    #     #             config_results = gen_config_results

    #     #         config_dict[fnum] = config_results

    #     # elif 'pinto' in source_dir:
    #     #     gen_config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_pinto_basic.cfg'))
    #     #     for fnum in fnum_list:
    #     #         if os.path.exists(os.path.join(base_config_dir, 'SAXS_pinto_{:03d}.cfg'.format(fnum))):
    #     #             config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_pinto_{:03d}.cfg'.format(fnum)))
    #     #         else:
    #     #             config_results = gen_config_results

    #     #         config_dict[fnum] = config_results

    #     # elif 'sosnick' in source_dir:
    #     #     if len(fnum_list) == 30:
    #     #         prefix='short'
    #     #     else:
    #     #         prefix='long'

    #     #     gen_config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_sosnick_{}_basic.cfg'.format(prefix)))
    #     #     for fnum in fnum_list:
    #     #         if os.path.exists(os.path.join(base_config_dir, 'SAXS_sosnick_{}_{:03d}.cfg'.format(prefix, fnum))):
    #     #             config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_sosnick_{}_{:03d}.cfg'.format(prefix, fnum)))
    #     #         else:
    #     #             config_results = gen_config_results

    #     #         config_dict[fnum] = config_results

    #     # elif 'cytc' in source_dir:
    #     #     # if fprefix in ['native_cytc1', 'native_buffer1']:
    #     #     #     prefix = 'native'
    #     #     # elif fprefix in ['buffer2', 'buffer3', 'cytc2', 'cytc3']:
    #     #     #     prefix = '0808'
    #     #     # elif fprefix in ['buffer4' , 'buffer5', 'cytc4', 'cytc5']:
    #     #     #     prefix = '0809'

    #     #     # gen_config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_cytc_{}_basic.cfg'.format(prefix)))

    #     #     # for fnum in fnum_list:
    #     #     #     if os.path.exists(os.path.join(base_config_dir, 'SAXS_cytc_{}_{:03d}.cfg'.format(prefix, fnum))):
    #     #     #         config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_cytc_{}_{:03d}.cfg'.format(prefix, fnum)))
    #     #     #     else:
    #     #     #         config_results = gen_config_results

    #     #     #     config_dict[fnum] = config_results

    #     #     gen_config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_cytc_basic.cfg'))
    #     #     for fnum in fnum_list:
    #     #         if os.path.exists(os.path.join(base_config_dir, 'SAXS_cytc_{:03d}.cfg'.format(fnum))):
    #     #             config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'SAXS_cytc_{:03d}.cfg'.format(fnum)))
    #     #         else:
    #     #             config_results = gen_config_results

    #     #         config_dict[fnum] = config_results


    #     # # December 2019
    #     # if 'martin' in source_dir.lower():
    #     #     for fnum in fnum_list:
    #     #         print fnum
    #     #         # gen_config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'em_basic_{:04d}.cfg'.format(fnum)))
    #     #         gen_config_results = raw.load_settings(os.path.join(base_config_dir, 'em_basic_{:04d}.cfg'.format(fnum)))
    #     #         for step in step_list:
    #     #             print step
    #     #             if os.path.exists(os.path.join(base_config_dir, 'em_{}_{:04d}.cfg'.format(step, fnum))):
    #     #                 # print os.path.join(base_config_dir, 'em_{}_{:04d}.cfg'.format(step, fnum))
    #     #                 # config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'em_{}_{:04d}.cfg'.format(step, fnum)))
    #     #                 config_results = raw.load_settings(os.path.join(base_config_dir, 'em_{}_{:04d}.cfg'.format(step, fnum)))
    #     #             else:
    #     #                 # print 'basic'
    #     #                 config_results = gen_config_results

    #     #             config_dict[(fnum, step)] = config_results

    #     # elif 'pinto' in source_dir.lower():
    #     #     for fnum in fnum_list:
    #     #         print fnum
    #     #         # gen_config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'em_basic_{:04d}.cfg'.format(fnum)))
    #     #         gen_config_results = raw.load_settings(os.path.join(base_config_dir, 'jp_basic_{:04d}.cfg'.format(fnum)))
    #     #         for step in step_list:
    #     #             print step
    #     #             if os.path.exists(os.path.join(base_config_dir, 'jp_{}_{:04d}.cfg'.format(step, fnum))):
    #     #                 # print os.path.join(base_config_dir, 'jp_{}_{:04d}.cfg'.format(step, fnum))
    #     #                 # config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'jp_{}_{:04d}.cfg'.format(step, fnum)))
    #     #                 config_results = raw.load_settings(os.path.join(base_config_dir, 'jp_{}_{:04d}.cfg'.format(step, fnum)))
    #     #             else:
    #     #                 # print 'basic'
    #     #                 config_results = gen_config_results

    #     #             config_dict[(fnum, step)] = config_results

    #     # elif '/na/' in source_dir.lower():
    #     #     na_list = ['ric_mgs_01', 'ric_01', 'ric452_mgs_01']
    #     #     na2_list = ['buf_01', 'ric452_mgs_02', 'ric452_mgs_03', 'ric452_01',
    #     #                     'ric_mgo_01', 'ric_mgo_02', 'buf_02', 'ric452_mgo_01', 'buf_03']

    #     #     if fprefix in na_list:
    #     #         cfg_prefix = 'na'
    #     #     elif fprefix in na2_list:
    #     #         cfg_prefix = 'na2'

    #     #     for fnum in fnum_list:
    #     #         print fnum
    #     #         # gen_config_results = saxs_raver.init_integration(os.path.join(base_config_dir, 'em_basic_{:04d}.cfg'.format(fnum)))
    #     #         gen_config_results = raw.load_settings(os.path.join(base_config_dir, '{}_basic_{:04d}.cfg'.format(cfg_prefix, fnum)))
    #     #         for step in step_list:
    #     #             print step
    #     #             if os.path.exists(os.path.join(base_config_dir, '{}_{}_{:04d}.cfg'.format(cfg_prefix, step, fnum))):
    #     #                 # print os.path.join(base_config_dir, '{}_{}_{:04d}.cfg'.format(step, fnum))
    #     #                 # config_results = saxs_raver.init_integration(os.path.join(base_config_dir, '{}_{}_{:04d}.cfg'.format(step, fnum)))
    #     #                 config_results = raw.load_settings(os.path.join(base_config_dir, '{}_{}_{:04d}.cfg'.format(cfg_prefix, step, fnum)))
    #     #             else:
    #     #                 # print 'basic'
    #     #                 config_results = gen_config_results

    #     #             config_dict[(fnum, step)] = config_results


    #     # # Laminar flow Dec. 2021
    #     # run_num = int(source_dir.split('/')[-1].lstrip('RM'))

    #     # if 1 <= run_num and run_num <= 5:
    #     #     sub_mask_dir = 'rm01_05'
    #     # elif run_num == 6:
    #     #     sub_mask_dir = 'rm06'
    #     # elif 8 <= run_num and run_num <= 10:
    #     #     sub_mask_dir = 'rm08_10'
    #     # elif 12 <= run_num and run_num <= 13:
    #     #     sub_mask_dir = 'rm12_13'
    #     # elif run_num == 15:
    #     #     sub_mask_dir = 'rm15'
    #     # elif run_num == 16:
    #     #     sub_mask_dir = 'rm16'
    #     # elif 17 <= run_num and run_num <= 20:
    #     #     sub_mask_dir = 'rm17_20'
    #     # elif run_num == 21:
    #     #     sub_mask_dir = 'rm21'
    #     # elif run_num == 22:
    #     #     sub_mask_dir = 'rm22'

    #     # gen_config_results = raw.load_settings(os.path.join(base_config_dir, sub_mask_dir, 'rm_basic.cfg'))

    #     # for fnum in fnum_list:
    #     #     if os.path.exists(os.path.join(base_config_dir, sub_mask_dir, 'rm_{:04d}.cfg'.format(fnum))):
    #     #         config_results = raw.load_settings(os.path.join(base_config_dir, sub_mask_dir, 'rm_{:04d}.cfg'.format(fnum)))
    #     #     else:
    #     #         config_results = gen_config_results

    #     #     config_dict[fnum] = config_results



    #     # # Chaotic flow, April 2022

    #     # if 'Bilsel' in base_config_dir and 'short' not in base_config_dir:

    #     #     gen_config_results = raw.load_settings(os.path.join(base_config_dir, 'ob_basic.cfg'))

    #     #     for fnum in fnum_list:
    #     #         # print(fnum)
    #     #         if os.path.exists(os.path.join(base_config_dir, 'ob_{:04d}.cfg'.format(fnum))):
    #     #             config_results = raw.load_settings(os.path.join(base_config_dir, 'ob_{:04d}.cfg'.format(fnum)))
    #     #         else:
    #     #             config_results = gen_config_results

    #     #         config_dict[fnum] = config_results

    #     # elif 'Bilsel' in base_config_dir and 'short' in base_config_dir:

    #     #     gen_config_results = raw.load_settings(os.path.join(base_config_dir, 'ob_basic.cfg'))

    #     #     for fnum in fnum_list:
    #     #         # print(fnum)
    #     #         if os.path.exists(os.path.join(base_config_dir, 'ob_{:04d}.cfg'.format(fnum))):
    #     #             config_results = raw.load_settings(os.path.join(base_config_dir, 'ob_{:04d}.cfg'.format(fnum)))
    #     #         else:
    #     #             config_results = gen_config_results

    #     #         config_dict[fnum] = config_results

    #     # elif 'cytc' in base_config_dir:
    #     #     gen_config_results = raw.load_settings(os.path.join(base_config_dir, 'cytc_basic.cfg'))

    #     #     for fnum in fnum_list:
    #     #         # print(fnum)
    #     #         if os.path.exists(os.path.join(base_config_dir, 'cytc_{:04d}.cfg'.format(fnum))):
    #     #             config_results = raw.load_settings(os.path.join(base_config_dir, 'cytc_{:04d}.cfg'.format(fnum)))
    #     #         else:
    #     #             config_results = gen_config_results

    #     #         config_dict[fnum] = config_results


    #     gen_config_results = raw.load_settings(os.path.join(mask_dir, '{}_basic.cfg'.format(mask_prefix)))

    #     for fnum in fnum_list:
    #         # print(fnum)
    #         if os.path.exists(os.path.join(mask_dir, '{}_{:04d}.cfg'.format(mask_prefix, fnum))):
    #             config_results = raw.load_settings(os.path.join(mask_dir, '{}_{:04d}.cfg'.format(mask_prefix, fnum)))
    #             # print('point config')
    #         else:
    #             config_results = gen_config_results
    #             # print('generic config')

    #         config_dict[fnum] = config_results

    #     print('Processing images')
    #     for name, stuff in diff_list:
    #         print(name)

    #         fnum = int(os.path.splitext(name)[0].split('_')[-1])
    #         # step = name.split('_')[-3]
    #         # ai, mask, q_range, maxlen, normlist, do_normalization, raw_settings, calibrate_dict, fliplr, flipud = config_dict[(fnum, step)]
    #         # raw_settings = config_dict[(fnum, step)]
    #         raw_settings = config_dict[fnum]
    #         # start_point = raw_settings.get('StartPoint')
    #         # end_point = raw_settings.get('EndPoint')

    #         # saxs_raver.doIntegration(output_dir, ai, mask, q_range,
    #         #     maxlen, normlist, do_normalization, calibrate_dict,
    #         #     start_point, end_point, fliplr, flipud,
    #         #     os.path.join(source_dir, name))

    #         a = time.time()
    #         dats, _ = raw.load_and_integrate_images([os.path.join(source_dir,name)], raw_settings)
    #         print(time.time()-a)
    #         data = dats[0]

    #         raw.save_profile(data, settings=raw_settings, datadir=output_dir)

    # except KeyboardInterrupt:
    #     break
