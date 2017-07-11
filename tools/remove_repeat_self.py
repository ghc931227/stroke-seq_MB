#!/usr/bin/env python  
#-*- coding: UTF-8 -*-
import sys;  
#删除第一个文件中的重复行，并生成第二个文件

lines_seen = set() 
outfile = open(sys.argv[2],"w")
for line in open(sys.argv[1],"r"):
    if line not in lines_seen:
        outfile.write(line)
        lines_seen.add(line)
outfile.close()

