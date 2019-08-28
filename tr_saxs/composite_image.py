import fabio
import os.path
import glob
import numpy as np
from PIL import Image

# #Input params
# image_dir = '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/images/cytc/20181202'
# image_prefix = 'b-cytc'
# start_num = 1
# end_num = 1988

# #Output params
# output_dir = '/nas_data/Pilatus1M/2018_Run3/20181130Bilsel/processing'

# img_list = [os.path.join(image_dir, '{}_{:05d}.tif'.format(image_prefix, i)) for i in range(start_num, end_num+1)]

# img = fabio.open(img_list[0])
# comp_img = np.zeros_like(img.data)

# for img_name in img_list:
#     print os.path.basename(img_name)
#     img = fabio.open(img_name)
#     comp_img = comp_img + img.data


# im = Image.fromarray(comp_img)
# im.save(os.path.join(output_dir, '{}_composite_{}_{}.tif'.format(image_prefix, start_num, end_num)))


#Input params
top_dir = '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/martin'
sub_dirs = ['buffer1', 'buffer2', 'buffer3', 'buffer4', 'em1', 'em2']

fdir = os.path.join(top_dir, sub_dirs[0])

f_list = glob.glob(os.path.join(fdir, '{}_*_0001_*.tif'.format(sub_dirs[0])))
fnum_list = [int(fname.split('_')[-1].strip('.tif')) for fname in f_list]
fnum_list.sort()

sample_image = fabio.open(f_list[0])
img_list = [np.zeros_like(sample_image.data) for i in range(len(fnum_list))]

for my_dir in sub_dirs:
    print my_dir
    for j, fnum in enumerate(fnum_list):
        print fnum
        imgs = glob.glob(os.path.join(top_dir, my_dir, '{}_*_{:04d}.tif'.format(my_dir, fnum)))
        for img_name in imgs:
            img = fabio.open(img_name)
            img_list[j] = img_list[j] + img.data

#Output params
output_dir = '/nas_data/Pilatus1M/2019_Run2/20190807Srinivas/processing/composite_images'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for j, img in enumerate(img_list):
    im = Image.fromarray(img)
    im.save(os.path.join(output_dir, '{}_composite_{:04d}.tif'.format(os.path.split(top_dir)[-1], fnum_list[j])))
