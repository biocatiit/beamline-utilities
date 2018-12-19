# Python script to renumber the cf-saxs data. 
# Also modified to add a scan number to standard sec-saxs data 
# The data format is assumed to be in the following format: 
# 
# basefilename_123456.ext  (where .ext is typically .dat)  
# 
# output ends up looking like: 
# 
# basefilename_1234_1234.ext 
# 
# where the first 1234 is the scan number and the second 1234 is the frame num. 
# To execute the program: 
# 
# python renumber-files.py "./dir/basefilename*" frames [ --check --doit ] | sort | more  
# Osman 4/29/2015 
# 3/28/2016 
#
# Sagar 12/09/2016 
#
# Modified this to start numbering from 1 and to handle arbitrary base file
# file length (Osman)
#
# 12/20/2016 Modified for use with Python3.4.  
# Handles any number of characters for frame# field and basefilename, e.g.:
# basefilename_123456789.dat.
# Output is still always in the format of basefilename_1234_1234.dat (scan#_frame#).
# -Osman

import sys 
import os 
import glob 
from shutil import copyfile

print("argv:")
for x in sys.argv:
   print(x)

print(" ")

if len(sys.argv) < 4:
   print("Usage: python renumber-files.py \"/sourcedir/basefilename*\" frames --check")
   print("       python renumber-files.py \"/sourcedir/basefilename*\" frames --doit")
   print(" ")
   print("Can add \" |more\" for readability display" )
   print("Copies renumbered files from source dir to current directory." )

else:
  frames = int(sys.argv[2])
  file_list = glob.glob(sys.argv[1])
  file_list.sort(key=lambda x: int(x.split('_')[-1].split('.')[0]))

  for path in file_list: 
    #print("--------------")
    path, filename = os.path.split(path) 
    fname, ext = os.path.splitext(filename)

    base_file_name, old_frame_num = fname.split('_')
    old_frame_num = int(old_frame_num) -1

    new_scan_num, new_frame_num = divmod(old_frame_num, frames)
    new_frame_num = new_frame_num + 1
    new_scan_num = new_scan_num + 1

    new_file_name = './%s_%04i_%04i%s' %(base_file_name, new_scan_num, new_frame_num, ext)

    # index_base=filename.find('_')
    # basefilename=filename[:index_base]
    # index_extension=filename.find('.')
    # ext=filename[index_extension:index_extension+4]
    """
    print("index_base: ",index_base)
    print("index_extension: ", index_extension)
    print("basefilename: ",basefilename)
    print("ext: ",ext)
    print("filename: ", filename)
    print("frame string: ", filename[index_base+1:index_extension])  
    """
    # oldframenum = int(float(filename[index_base+1:index_extension])) - 1 
    # x = divmod(oldframenum, frames) 
    # newscannum = 10001 + x[0] 
    # newframenum = 10001 + x[1] 
    """
    print("--------------")
    print("oldframenum: ",oldframenum)
    print("divmod result: ", x)
    print("newscannum, newframenum: ",newscannum, newframenum)
    """
    # scanstr = str(newscannum)[1:] 
    # framestr = str(newframenum)[1:] 
    # #print("path, filename, scanstr: ", path, filename, scanstr)
    # newfilename = "./" + basefilename + "_" + scanstr + "_" + framestr + ext 

    print(filename," ===> ", new_file_name) 
  
    if sys.argv[3] == "--doit": 
      copyfile(os.path.join(path,filename),new_file_name)


