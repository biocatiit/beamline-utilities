import hdf5plugin
import fabio
import os.path
import glob
import numpy as np
from PIL import Image

# # Chaotic flow

# # #Input params
# # image_dir = '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/cytc/20181202'
# # image_prefix = 'b-cytc'
# # start_num = 1
# # end_num = 1988

# # #Output params
# # output_dir = '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/processing'

# # img_list = [os.path.join(image_dir, '{}_{:05d}.tif'.format(image_prefix, i)) for i in range(start_num, end_num+1)]

# # img = fabio.open(img_list[0])
# # comp_img = np.zeros_like(img.data)

# # for img_name in img_list:
# #     print os.path.basename(img_name)
# #     img = fabio.open(img_name)
# #     comp_img = comp_img + img.data


# # im = Image.fromarray(comp_img)
# # im.save(os.path.join(output_dir, '{}_composite_{}_{}.tif'.format(image_prefix, start_num, end_num)))


# #Input params
# # top_dir = '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/martin'
# # sub_dirs = ['buffer1', 'buffer2', 'buffer3', 'buffer4', 'em1', 'em2']

# #Sosnick short scans
# # top_dir = '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick'
# # sub_dirs = ['buffer2', 'buffer4', 'buffer5', 'buffer6', 'buffer7', 'buffer8',
# #     'buffer9', 'buffer10', 'ub1', 'ub3', 'ub4', 'ub5', 'ub6', 'ub7', 'ub8', 'ub9',
# #     'ub10', 'ub11', 'ub12']

# #Sosnick long scans
# # top_dir = '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/sosnick'
# # sub_dirs = ['buffer3', 'ub2']

# #Pinto scans
# # top_dir = '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/pinto'
# # sub_dirs = ['buffer1', 'twt1', 'twt2', 'twt3', 'tmt1', 'tmt2', 'tmt3']

# #Native cytc
# # top_dir = '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/cytc'
# # sub_dirs = ['native_buffer1', 'native_cytc1']

# #Refolding cytc, 8/8
# # top_dir = '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/cytc'
# # sub_dirs = ['buffer2', 'buffer3', 'cytc2' 'cytc3']

# # # #Refolding cytc, 8/9
# # top_dir = '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/cytc'
# # sub_dirs = ['buffer4', 'buffer5', 'cytc4' 'cytc5']

# # Dec. 2019 chaotic
# # top_dir = '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_chaotic'
# # sub_dirs = ['buf_01', 'buf_02', 'buf_03' 'buf_04', 'buf_05', 'em_01', 'em_02',
# #     'em_03', 'em_04']

# # top_dir = '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/pinto_chaotic'
# # sub_dirs = ['buf_01', 'buf_02', 'buf_03' 'buf_04', 'buf_05', 'twt_01', 'twt_02',
# #     'twt_03', 'twt_04']

# top_dir = '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cytc_2'
# sub_dirs = ['buf2_01', 'buf2_02', 'buf2_03', 'cytc2_01', 'cytc2_02']


# Dec. 2021 chaotic
# top_dir = '/nas_data/Pilatus1M/2021_Run3/20211219_Monsen'
# sub_dirs = ['RM01', 'RM02', 'RM03', 'RM04', 'RM05']
# sub_dirs = ['RM06']
# sub_dirs = ['RM08', 'RM09', 'RM10']
#sub_dirs = ['RM12', 'RM13']
# sub_dirs = ['RM15']
# sub_dirs = ['RM16']
# sub_dirs = ['RM17', 'RM19', 'RM20']
# sub_dirs = ['RM21']
# sub_dirs = ['RM22']

# # April 2022 chaotic
# img_ext = 'h5'
# extra_name = 'data'
# zpad = 6
# # top_dir = '/nas_data/Eiger2xe9M/2022_Run1/20220420_Hopkins/setup/water'
# # sub_dirs = ['water01', 'water02', 'water03']

# # top_dir = '/nas_data/Eiger2xe9M/2022_Run1/20220420_Hopkins/lysozyme/refolding'
# # sub_dirs = ['lys_01', 'lys_02', 'lys_03', 'lys_04', 'lys_05', 'lys_06', 'lys_07']

# # top_dir = '/nas_data/Eiger2xe9M/2022_Run1/20220420_Hopkins/lysozyme/refolding'
# # sub_dirs = ['lys_08', 'lys_09', 'lys_10']

# top_dir = '/nas_data/Eiger2xe9M/2022_Run1/20220420_Hopkins/CytC/native'
# sub_dirs = ['native01', 'native02', 'native03']

# # top_dir = '/nas_data/Eiger2xe9M/2022_Run1/20220420_Hopkins/CytC/refolding'
# # sub_dirs = ['cytc_01', 'cytc_02', 'cytc_03', 'cytc_04', 'cytc_06']

# # top_dir = '/nas_data/Eiger2xe9M/2022_Run1/20220423_Bilsel'
# # sub_dirs = ['OB03', 'OB04']

# # top_dir = '/nas_data/Eiger2xe9M/2022_Run1/20220423_Bilsel'
# # sub_dirs = ['OB06', 'OB07', 'OB08', 'OB09',' OB10', 'OB11', 'OB12']


# #Output params
# # output_dir = '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/cf_processing/composite_images'
# output_dir = '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/composite_images/cytc'
# output_dir = '/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/processing/composite_images/rm01_05'
# output_dir = '/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/processing/composite_images/rm06'
# output_dir = '/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/processing/composite_images/rm08_10'
#output_dir = '/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/processing/composite_images/rm12_13'
# output_dir = '/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/processing/composite_images/rm15'
# output_dir = '/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/processing/composite_images/rm16'
# output_dir = '/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/processing/composite_images/rm17_20'
# output_dir = '/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/processing/composite_images/rm21'
# output_dir = '/nas_data/Pilatus1M/2021_Run3/20211219_Monsen/processing/composite_images/rm22'
# output_dir = '/nas_data/Eiger2xe9M/2022_Run1/20220420_Hopkins/processing/composite_images/water01_03'
# output_dir = '/nas_data/Eiger2xe9M/2022_Run1/20220420_Hopkins/processing/composite_images/lys/refolding_full'
# output_dir = '/nas_data/Eiger2xe9M/2022_Run1/20220423_Bilsel/processing/composite_images'
# output_dir = '/nas_data/Eiger2xe9M/2022_Run1/20220423_Bilsel/processing/composite_images/short'
# output_dir = '/nas_data/Eiger2xe9M/2022_Run1/20220420_Hopkins/processing/composite_images/cytc/refolding'
# output_dir = '/nas_data/Eiger2xe9M/2022_Run1/20220420_Hopkins/processing/composite_images/lys/refolding_short'
# output_dir = '/nas_data/Eiger2xe9M/2022_Run1/20220420_Hopkins/processing/composite_images/cytc/native'



# April 2023 chaotic
img_ext = 'h5'
extra_name = 'data'
zpad = 6
images_subdir = True

# top_dir = '/nas_data/Eiger2x/2023_Run1/20230405_Pollack'
# sub_dirs = ['LP01/images', 'LP02/images', 'LP03/images', 'LP04/images']
# output_dir = '/nas_data/Eiger2x/2023_Run1/20230405_Pollack/processing/composite_images/day1'

# top_dir = '/nas_data/Eiger2x/2023_Run1/20230405_Pollack'
# sub_dirs = ['LP07/images', 'LP08/images',]
# output_dir = '/nas_data/Eiger2x/2023_Run1/20230405_Pollack/processing/composite_images/day2'

# top_dir = '/nas_data/Eiger2x/2023_Run1/20230405_Pollack'
# sub_dirs = ['LP11/images', 'LP12/images', 'LP13/images',]
# output_dir = '/nas_data/Eiger2x/2023_Run1/20230405_Pollack/processing/composite_images/day3'

# top_dir = '/nas_data/Eiger2x/2023_Run1/20230409_Gupta'
# sub_dirs = ['KG03/images', 'KG04/images', 'KG05/images', 'KG06/images', 'KG07/images',
#     'KG08/images', 'KG09/images', 'KG10/images', 'KG11/images', 'KG12/images',]
# output_dir = '/nas_data/Eiger2x/2023_Run1/20230409_Gupta/processing/composite_images'

# top_dir = '/nas_data/Eiger2x/2023_Run1/20230412_Ho'
# sub_dirs = ['MH01/images', 'MH02/images', 'MH03/images', 'MH04/images', 'MH05/images', 
#     'MH06/images',]
# output_dir = '/nas_data/Eiger2x/2023_Run1/20230412_Ho/processing/composite_images/day1'

# top_dir = '/nas_data/Eiger2x/2023_Run1/20230412_Ho'
# sub_dirs = ['MH07/images', 'MH08/images', 'MH09/images', 'MH10/images', 'MH11/images',
#     'MH12/images', 'MH13/images', 'MH14/images', 'MH15/images', 'MH16/images',
#     'MH17/images', 'MH18/images',]
# output_dir = '/nas_data/Eiger2x/2023_Run1/20230412_Ho/processing/composite_images/day2'

top_dir = '/nas_data/Eiger2x/2023_Run1/20230415_Juarez'
sub_dirs = ['OJ02/images', 'OJ03/images', 'OJ04/images', 'OJ05/images', 'OJ06/images',
    'OJ07/images', 'OJ08/images', 'OJ09/images', 'OJ10/images',]
output_dir = '/nas_data/Eiger2x/2023_Run1/20230415_Juarez/processing/composite_images'


fdir = os.path.join(top_dir, sub_dirs[0])

if images_subdir:
    prefix = os.path.split(sub_dirs[0])[0]
else:
    prefix = sub_dirs[0]

f_list = glob.glob(os.path.join(fdir, '{}_*_0001_{}*.{}'.format(prefix, extra_name, img_ext)))
fnum_list = list(set([int(fname.split('_')[-1].rstrip('{}'.format(img_ext)).rstrip('.')) for fname in f_list]))
fnum_list.sort()

sample_image = fabio.open(f_list[0])
img_list = [np.zeros_like(sample_image.data) for i in range(len(fnum_list))]

for my_dir in sub_dirs:
    print(my_dir)
    for j, fnum in enumerate(fnum_list):
        print(fnum)
        if images_subdir:
            prefix = os.path.split(my_dir)[0]
        else:
            prefix = my_dir
        imgs = glob.glob(os.path.join(top_dir, my_dir, '{}_*{}_{:0{}d}.{}'.format(prefix, extra_name, fnum, zpad, img_ext)))
        for img_name in imgs:
            img = fabio.open(img_name)
            img_list[j] = img_list[j] + img.data



print('Saving composite images')


if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for j, img in enumerate(img_list):
    im = Image.fromarray(img)
    im.save(os.path.join(output_dir, '{}_composite_{:04d}.tif'.format(os.path.split(top_dir)[-1], fnum_list[j])))
    # im.save(os.path.join(output_dir, '{}_composite_{:04d}.tif'.format('cc_1217', fnum_list[j])))

tot_im = np.sum(np.array(img_list), axis=0)
tot_im = Image.fromarray(tot_im.astype(np.int32))
tot_im.save(os.path.join(output_dir, '{}_composite_total.tif'.format(os.path.split(top_dir)[-1])))

# # Laminar flow

# # top_dir = '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_laminar'
# # sub_dirs = ['em01', 'em02', 'em03', 'em04', 'em05', 'em06', 'em07', 'em08',
# #     'em09', 'em10']

# # top_dir = '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_laminar'
# # sub_dirs = ['em01', 'em02', 'em03', 'em04', 'em05', 'em06', 'em07', 'em08',
# #     'em09', 'em10']

# # top_dir = '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/2019_1210Pinto'
# # sub_dirs = ['mt_01', 'mt_02', 'mt_03', 'wt_01', 'wt_02', 'wt_03', 'wt_e',
# #     'wt_eq_01', 'wt_eq_02']

# # top_dir = '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/na'
# # sub_dirs = ['ric_mgs_01', 'ric_01', 'ric452_mgs_01']
# # prefix = 'na'

# top_dir = '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/na'
# sub_dirs = ['buf_01', 'ric452_mgs_02', 'ric452_mgs_03', 'ric452_01',
#     'ric_mgo_01', 'ric_mgo_02', 'buf_02', 'ric452_mgo_01', 'buf_03']
# prefix = 'na2'

# # top_dir = '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/bsa'
# # sub_dirs = ['bsa_sds_01', 'bsa_sds_02', 'bsa_sds_03', 'bsa_equilib']
# # prefix = 'bsa'

# fdir = os.path.join(top_dir, sub_dirs[0])

# f_list = glob.glob(os.path.join(fdir, '{}_???_s???_0001_*.tif'.format(sub_dirs[0]))) # For martin
# if len(f_list) == 0:
#     f_list = glob.glob(os.path.join(fdir, '{}_???_s????_0001_*.tif'.format(sub_dirs[0]))) #

# fnum_list = list(set([int(fname.split('_')[-1].strip('.tif')) for fname in f_list]))
# fnum_list.sort()
# step_list = list(set([fname.split('_')[-3] for fname in f_list]))
# step_list.sort()

# sample_image = fabio.open(f_list[0])
# step_img_list = [[np.zeros_like(sample_image.data) for i in range(len(fnum_list))] for i in range(len(step_list))]

# for my_dir in sub_dirs:
#     print my_dir
#     for k, step in enumerate(step_list):
#         print step
#         for j, fnum in enumerate(fnum_list):
#             print fnum
#             imgs = glob.glob(os.path.join(top_dir, my_dir, '{}_???_{}_????_{:04d}.tif'.format(my_dir, step, fnum)))
#             # print imgs
#             # print '{}_???_{}_{:04d}.tif'.format(my_dir, step, fnum)
#             for img_name in imgs:
#                 img = fabio.open(img_name)
#                 step_img_list[k][j] = step_img_list[k][j] + img.data

# #Output params
# output_dir = '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/composite_images/{}'.format(prefix)

# if not os.path.exists(output_dir):
#     os.makedirs(output_dir)

# for k, step in enumerate(step_list):
#     for j, fnum in enumerate(fnum_list):
#         im = Image.fromarray(step_img_list[k][j])
#         im.save(os.path.join(output_dir, '{}_composite_{}_{:04d}.tif'.format('{}_1210'.format(prefix), step, fnum)))
