#!/usr/bin/env python  
#-*- coding: UTF-8 -*-
import sys;  
#从他人分享的复杂码表提取拼音词库，拼音在前，每字拼音以分隔符“'”隔开(例如：'fang'an 和 'fan'gan)，tab后跟汉字,保存为新文件
#也可用于从码表中提取特定字段。

fc=open(sys.argv[2],'w')

with open(sys.argv[1], 'rb') as f:
    for line in f:
        p=""
        pp=0
        temp_fb = line.replace('-','\'').replace('\n','').split('\t')    #把-换为'，去除回车号，以空格或tab分割
#        print 'temp_fb[0]=',temp_fb[0],'temp_fb[1]=',temp_fb[1],'\n',  #打印检查分割效果      
        p=temp_fb[4]
        ppp=1000-int(p)                                                #字频重排，降序改升序
#        print 'temp_fb[4]=',temp_fb[1],'p=',p,'ppp=',ppp,
        fc.write(''.join(temp_fb[1]+'\t'+temp_fb[3]+'\t'+str(ppp)+'\n'))     # 写入文件，以tab分割，注意选择恰当的字段

