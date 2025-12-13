import hdf5plugin
import fabio
import os.path
import glob
import numpy as np
from PIL import Image

img_ext = 'h5'
extra_name = 'data'
zpad = 6
images_subdir = False

# Laminar
top_dir = '/nas_data/Eiger2x/2025_Run3/2025_12_12_Grubic'
sub_dirs = ['TG06']
output_dir = '/nas_data/Eiger2x/2025_Run3/2025_12_12_Grubic/processing/composite_images_12_13'

max_images = 50

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

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
        for img_name in imgs[:max_images]:
            img = fabio.open(img_name)
            img_list[j] = img_list[j] + img.data

        im = Image.fromarray(img_list[j])
        im.save(os.path.join(output_dir, '{}_composite_{:04d}.tif'.format(my_dir, fnum_list[j])))


# if not os.path.exists(output_dir):
#     os.makedirs(output_dir)

# for j, img in enumerate(img_list):
#     im = Image.fromarray(img)
#     im.save(os.path.join(output_dir, '{}_composite_{:04d}.tif'.format(os.path.split(top_dir)[-1], fnum_list[j])))
#     # im.save(os.path.join(output_dir, '{}_composite_{:04d}.tif'.format('cc_1217', fnum_list[j])))

tot_im = np.sum(np.array(img_list), axis=0)
tot_im = Image.fromarray(tot_im.astype(np.int32))
tot_im.save(os.path.join(output_dir, '{}_composite_total.tif'.format(os.path.split(top_dir)[-1])))
