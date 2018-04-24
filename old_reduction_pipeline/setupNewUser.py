# -*- coding: utf-8 -*-
import sys
import os
import datetime

print "Usage: python setupNewUser.py groupname"

PI_name = sys.argv[1]

logRoot = '/nas_data/SAXS_Logfiles/'
usrRoot = '/nas_data/SAXS_Data/'
tifRoot = '/nas_data/Pilatus1M/'

now = datetime.datetime.now()
userFolder = "%04d%02d%02d%s" %(now.year, now.month, now.day, PI_name)
print "Folder to be created: " + userFolder

def createFolderInPath(folder, path):
  p = os.path.join(path, folder)
  if os.path.exists(p):
    print p+" = Folder exists! Nothing done!" 
  else:
    os.system('mkdir ' + p)
    os.system('chmod go+w ' + p)
    print p+" = created!"

createFolderInPath(userFolder, logRoot)
createFolderInPath(userFolder, usrRoot)
createFolderInPath(userFolder, tifRoot)

