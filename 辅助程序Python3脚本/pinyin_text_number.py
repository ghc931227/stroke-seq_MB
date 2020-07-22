#!/usr/bin/env python  
#-*- coding: UTF-8 -*-
import os
import sys;
import codecs;
reload(sys)
sys.setdefaultencoding("utf-8")
#重新整理他人分享的拼音词库文件，拼音在前，每字拼音以分隔符“'”隔开(例如：'fang'an 和 'fan'gan)，空格后跟汉字,保存为新文件

fc=open(sys.argv[2],'w')

with open(sys.argv[1], 'rb') as f:
    for line in f:
        line2=unicode(line,'utf-8')
        temp_fb = line2.replace('-','\'').replace('\n','').split('\t')    #把-换为'，去除回车号，以空格或tab分割
#        m = temp_fb[0][-1].isdigit()                                      #判断字符串是否以数字结尾
#        if m is False:
#            print 'temp_fb[0]=',temp_fb[0],'temp_fb[1]=',temp_fb[1],'\n',  #打印检查分割效果     
#        temp_fb[1]=unicode(temp_fb[1],'utf-8')
        temp_fb[0] = temp_fb[0][:-1]                                  #删除字符串最后一个字符
        fc.write(''.join(temp_fb[0]+'\t'+temp_fb[1]+'\n')) # 写入文件，以tab分割

