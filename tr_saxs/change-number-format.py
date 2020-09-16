# Python script to reduce the number of digits in frame number from 5 to 4
# for cf-saxs data. 
# Also modified to add a scan number to standard sec-saxs data 
# The data format is assumed to be in the following format: 
# 
# input data filename format:
# bhasefilename_1234_01234.ext  (where .ext is typically .dat)  
# 
# output ends up looking like: 
# 
# basefilename_1234_1234.ext 
# 
# where the first 1234 is the scan number and the second 1234 is the frame num. 
# To execute the program: 
# 
# python change-number-format.py "./dir/basefilename*"  [ --check --doit ] | sort | more  
# Osman 5/22/2017 
#
#
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

if len(sys.argv) < 3:
   print("Usage: python renumber-files.py \"/sourcedir/basefilename*\"  --check")
   print("       python renumber-files.py \"/sourcedir/basefilename*\"  --doit")
   print(" ")
   print("Can add \"|sort  |more\" for sequential display" )
   print("Copies renumbered files from source dir to current directory." )

else:
  #frames = int(sys.argv[2]) 
  for path in glob.glob(sys.argv[1]): 
    #print("--------------")
    path, filename = os.path.split(path) 
    index_extension=filename.find('.')
    ext=filename[index_extension:index_extension+4]
    index_frame=index_extension-6
    index_scan=index_frame-5
    basefilename=filename[:index_scan]

    #print("index_scan: ",index_scan)
    #print("index_frame: ",index_frame)
    #print("index_extension: ", index_extension)
    #print("basefilename: ",basefilename)
    #print("ext: ",ext)
    #print("filename: ", filename)
    #print("scan string: ", filename[index_scan+1:index_frame])  
    #print("old frame string: ", filename[index_frame+1:index_extension])  
    #print("new frame string: ", filename[index_frame+2:index_extension])  

    
    scanstr = filename[index_scan+1:index_frame]  
    framestr = filename[index_frame+2:index_extension]  

    #print("path, filename, scanstr: ", path, filename, scanstr)
    newfilename = "./" + basefilename + "_" + scanstr + "_" + framestr + ext 

    print(filename," ===> ", newfilename) 
  
    if sys.argv[2] == "--doit": 
      copyfile(os.path.join(path,filename),newfilename)

