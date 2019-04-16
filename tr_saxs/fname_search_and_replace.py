# Python script to replace input_string in the base filename with output_string.
# The data format is assumed to be in the following format:
#
# basefilename1234_1234.tif.dat
# 
# output ends up looking like:
#
# basefilename_0001_1234.dat
#
# where the first 0001 is the scan number and the second 0001 is the frame num.
#
# after running 
#  python fname_replace.py "/dir/*" "basefilename1" "basefilename_1"  [ --doit ]
#  python fname_replace.py "/dir/*" ".tif.dat"  ".dat"     [ --doit ] 
#
#
#
# Osman
#       5/22/2017

import sys
import os
import glob
import string


print("--------------")
print("argv:")
print("(1) source_dir: ", sys.argv[1])
print("(2) search_string: ", sys.argv[2])
print("(3) replace_string: ", sys.argv[3])
if len(sys.argv) > 4:
   print("(4) do it?: ", sys.argv[4])

#print("--------------")
#print("argv:")
#for x in sys.argv:
#   print(x)

print(" ")


if len(sys.argv) < 4:
   print("Usage: python fname_search_and_replace.py \"/sourcedir/basefilename*\" \"search_str\" \"replace_string\" --doit")


for path in glob.glob(sys.argv[1]):
    print("--------------")
    path, filename = os.path.split(path) 
    #print("filename= ", filename)
    newfilename=filename.replace(sys.argv[2], sys.argv[3])
    #print("newfilename= ", newfilename)
  
    print(filename,"  ===>  ", newfilename)

    if len(sys.argv) > 4:
      if sys.argv[4] ==  "--doit":
        os.rename(filename, os.path.join(path,newfilename))
   
