#-*- coding: UTF-8 -*-
import re
import sys
import os

#判断B文件（想新增）中的汉字部分，是否有A文件（黑名单）的内容，没有就写入C
 
fa=open(sys.argv[1]).readlines()
fb=open(sys.argv[2]).readlines()
fc=open(sys.argv[3],'w')

with open(sys.argv[2], 'rb') as f:
    for line in f:
        temp_fb = line.split(' ') #以空格分割
#        print 'temp_fb[0]=',temp_fb[0],'temp_fb[1]=',temp_fb[1],'\n',  #打印检查分割效果
        if temp_fb[1] not in fa:                                #判断是否存在
            fc.write(''.join(temp_fb[0]+' '+temp_fb[1]))    #存在则把带拼音的写入新文件
        else:
            print temp_fb[1],


