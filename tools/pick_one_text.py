#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys;
import codecs;
reload(sys)
sys.setdefaultencoding("utf-8")
#读取第一个文件把每个汉字提取出来单独作为一行放入第二个文件

readfile = open(sys.argv[1]).readlines()
outfile = open(sys.argv[2],"w")

for i in readfile:
    lines=unicode(i,'utf-8')
#    print lines 

for j in lines:
#    print j
    outfile.write(j+'\n')
