#!/usr/bin/env python  
#-*- coding: UTF-8 -*-
import sys;  
#重新整理他人分享的拼音词库文件，拼音在前，每字拼音以分隔符“'”隔开(例如：'fang'an 和 'fan'gan)，空格后跟汉字,保存为新文件

fc=open(sys.argv[2],'w')

with open(sys.argv[1], 'rb') as f:
    for line in f:
        temp_fb = line.replace('-','\'').replace('\n','').split(' ') #把-换为'，去除回车号，以空格分割
#        print 'temp_fb[0]=',temp_fb[0],'temp_fb[1]=',temp_fb[1],'\n',  #打印检查分割效果
        fc.write(''.join(temp_fb[0]+' '+temp_fb[1]+'\n'))