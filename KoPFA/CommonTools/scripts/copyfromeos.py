#!/usr/bin/env python
import os
import re
import sys
import time
import commands
import KoPFA.CommonTools.eostools as castortools

path = sys.argv[1]
outpath = sys.argv[2]

print path

dirExit = castortools.runEOSCommand(path,'ls')
files = dirExit[0].split("\n")
for file in files:
  if not file:
    continue
  filepath=  path+"/"+file
  cmd = "xrdcp root://eoscms/"+filepath+" "+outpath
  os.system(cmd)


