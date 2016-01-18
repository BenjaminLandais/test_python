#!/usr/bin/env python

import os
import sys

def main(argv):

    if not len(sys.argv) == 2:
       print 'Usage: prout.py <src_directory>'
       sys.exit(2)

    ##Need to create a list ptf directory that ends in .git
    src_dir = str(sys.argv[1])
    ##Dirs to update with full path_name
    lines_to_insert = list()
    ##create the file file-name
    file_name = open("file-name", "a+")
    for root, dirs, files in os.walk(src_dir, topdown=True):
       for xml_file in files:
           ##print xml_file
           ##print os.path.join(root, xml_file);
           direc_and_file_name_concat = os.path.join(root, xml_file).replace(src_dir + "/","");
           ##print direc_and_file_name_concat
           line_to_ins = 'conf/project-name/' + direc_and_file_name_concat + '=>/opt/apache-tomcat6/conf/project-name/' + direc_and_file_name_concat
           ##print line_to_ins
           lines_to_insert.append(line_to_ins)

    for line_ins in lines_to_insert:
        file_name.write(line_ins + "\n")

    file_name.close()


if __name__ == "__main__":
  main(sys.argv[1:])
