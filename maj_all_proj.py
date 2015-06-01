#!/usr/bin/env python

import os
import sys
import subprocess
import git

def main(argv):

  if not len(sys.argv) == 2:
    print 'Usage: maj_all_proj.py <src_directory>'
    sys.exit(2)
  
  ##Need to create a list pf directory that ends in .git
  src_dir = str(sys.argv[1])
  ##Dirs to update with full path_name
  dirs_to_upd = list()

  for root, dirs, files in os.walk(src_dir, topdown=False):
    for directory in dirs:
      if directory.endswith(".git"):
        ##add dir to array
        dir_to_append = root
	dirs_to_upd.append(dir_to_append)
  
  for directory in dirs_to_upd:
    print "Updating " + directory
    ##subprocess.call('cd '+ directory, shell=True)
    ##subprocess.call('$PWD', shell=True)
    ##subprocess.call('git pull ' + directory, shell=True)
    g = git.cmd.Git(directory)
    g.pull()





if __name__ == "__main__":
   main(sys.argv[1:])																																					
