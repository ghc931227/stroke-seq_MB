#!/usr/bin/env python  
#-*- coding: UTF-8 -*-
import sys;  
#重新整理他人分享的拼音词库文件，拼音在前，每字拼音以分隔符“'”隔开(例如：'fang'an 和 'fan'gan)，空格后跟汉字,保存为新文件

fc=open(sys.argv[2],'w')

with open(sys.argv[1], 'rb') as f:
    temp_add = "'"
    for line in f:
#        temp_add = ""
#        if line[0] != "-":          # 如果开头没有 - 则添加 - ，统一格式。
#        print "line[0]=",line[0],'\n',"aa=",temp_add,'\n',             #打印检查分割效果

        temp_fb = line.replace('-','\'').replace('\n','').split('\t')    #把-换为'，去除回车号，以空格或tab分割
#        print 'temp_fb[0]=',temp_fb[0],'temp_fb[1]=',temp_fb[1],'\n',  #打印检查分割效果     
 
        temp_fc = temp_fb[0].split('/')                                 # 如果同一词有多个拼音，则以/分割
        for i in range(0, len(temp_fc)):                                # 如果同一词有多个拼音，则分开继续写入
             fc.write(temp_add+''.join(temp_fc[i]+'\t'+temp_fb[1]+'\n')) # 写入文件，以tab分割

