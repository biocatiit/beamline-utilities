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



# fdir = os.path.join(top_dir, sub_dirs[0])

# f_list = glob.glob(os.path.join(fdir, '{}_*_0001_*.tif'.format(sub_dirs[0])))
# fnum_list = [int(fname.split('_')[-1].strip('.tif')) for fname in f_list]
# fnum_list.sort()

# sample_image = fabio.open(f_list[0])
# img_list = [np.zeros_like(sample_image.data) for i in range(len(fnum_list))]

# for my_dir in sub_dirs:
#     print my_dir
#     for j, fnum in enumerate(fnum_list):
#         print fnum
#         imgs = glob.glob(os.path.join(top_dir, my_dir, '{}_*_{:04d}.tif'.format(my_dir, fnum)))
#         for img_name in imgs:
#             img = fabio.open(img_name)
#             img_list[j] = img_list[j] + img.data

# #Output params
# # output_dir = '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/cf_processing/composite_images'
# output_dir = '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/cf_processing/composite_images/cytc'

# if not os.path.exists(output_dir):
#     os.makedirs(output_dir)

# for j, img in enumerate(img_list):
#     im = Image.fromarray(img)
#     # im.save(os.path.join(output_dir, '{}_composite_{:04d}.tif'.format(os.path.split(top_dir)[-1], fnum_list[j])))
#     im.save(os.path.join(output_dir, '{}_composite_{:04d}.tif'.format('cc_1217', fnum_list[j])))



# Laminar flow

# top_dir = '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/martin_laminar'
# sub_dirs = ['em01', 'em02', 'em03', 'em04', 'em05', 'em06', 'em07', 'em08',
#     'em09', 'em10']

# top_dir = '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/2019_1210Pinto'
# sub_dirs = ['mt_01', 'mt_02', 'mt_03', 'wt_01', 'wt_02', 'wt_03', 'wt_e',
#     'wt_eq_01', 'wt_eq_02']

# top_dir = '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/na'
# sub_dirs = ['ric_mgs_01', 'ric_01', 'ric452_mgs_01']
# prefix = 'na'

top_dir = '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/na'
sub_dirs = ['buf_01', 'ric452_mgs_02', 'ric452_mgs_03', 'ric452_01',
    'ric_mgo_01', 'ric_mgo_02', 'buf_02', 'ric452_mgo_01', 'buf_03']
prefix = 'na2'

# top_dir = '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/bsa'
# sub_dirs = ['bsa_sds_01', 'bsa_sds_02', 'bsa_sds_03', 'bsa_equilib']
# prefix = 'bsa'

fdir = os.path.join(top_dir, sub_dirs[0])

# f_list = glob.glob(os.path.join(fdir, '{}_???_s???_0001_*.tif'.format(sub_dirs[0]))) # For martin
f_list = glob.glob(os.path.join(fdir, '{}_???_s????_0001_*.tif'.format(sub_dirs[0]))) #
fnum_list = list(set([int(fname.split('_')[-1].strip('.tif')) for fname in f_list]))
fnum_list.sort()
step_list = list(set([fname.split('_')[-3] for fname in f_list]))
step_list.sort()

sample_image = fabio.open(f_list[0])
step_img_list = [[np.zeros_like(sample_image.data) for i in range(len(fnum_list))] for i in range(len(step_list))]

for my_dir in sub_dirs:
    print my_dir
    for k, step in enumerate(step_list):
        print step
        for j, fnum in enumerate(fnum_list):
            print fnum
            imgs = glob.glob(os.path.join(top_dir, my_dir, '{}_???_{}_????_{:04d}.tif'.format(my_dir, step, fnum)))
            # print imgs
            # print '{}_???_{}_{:04d}.tif'.format(my_dir, step, fnum)
            for img_name in imgs:
                img = fabio.open(img_name)
                step_img_list[k][j] = step_img_list[k][j] + img.data

#Output params
output_dir = '/nas_data/Pilatus1M/2019_Run3/20191205Hopkins/lf_processing/composite_images/{}'.format(prefix)

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for k, step in enumerate(step_list):
    for j, fnum in enumerate(fnum_list):
        im = Image.fromarray(step_img_list[k][j])
        im.save(os.path.join(output_dir, '{}_composite_{}_{:04d}.tif'.format('{}_1210'.format(prefix), step, fnum)))
