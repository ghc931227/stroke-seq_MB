#!/usr/bin/env python  
#-*- coding: UTF-8 -*-

import re
import sys
import os

#判断B（带拼音大文件）文本中的内容在A（想新增拼音）文本里边，然后读取B文本中该拼音，得C
#注意所有文件都应保存成utf-8的文本文件。



fa=open(sys.argv[1]).readlines()
fc=open(sys.argv[3],'w')
k=0
with open(sys.argv[2], 'rb') as f:
    for line in f:
        temp_fb = line.split(' ') #以空格分割
#        print 'temp_fb[0]=',temp_fb[0],'temp_fb[1]=',temp_fb[1],'\n',  #打印检查分割效果
        if temp_fb[1] in fa:                                #判断是否存在
            fc.write(''.join(temp_fb[0]+' '+temp_fb[1]))    #存在则把带拼音的写入新文件
            k=k+1
            print k                      #去计数器，显示进度

