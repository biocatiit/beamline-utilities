import fabio
import os.path
import numpy as np
from PIL import Image

#Input params
image_dir = '/nas_data/Pilatus1M/20190807Srinivas/sosnick/ub2'
image_prefix = 'ub2_041_0001'
start_num = 1
end_num = 75

#Output params
output_dir = '/nas_data/Pilatus1M/20190807Srinivas/'

img_list = [os.path.join(image_dir, '{}_{:04d}.tif'.format(image_prefix, i)) for i in range(start_num, end_num+1)]

img = fabio.open(img_list[0])
comp_img = np.zeros_like(img.data)

for img_name in img_list:
    print os.path.basename(img_name)
    img = fabio.open(img_name)
    comp_img = comp_img + img.data


im = Image.fromarray(comp_img)
im.save(os.path.join(output_dir, '{}_composite_{}_{}.tif'.format(image_prefix, start_num, end_num)))
