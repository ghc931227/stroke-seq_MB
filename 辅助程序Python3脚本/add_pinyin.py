#!/usr/bin/env python  
#-*- coding: UTF-8 -*-

import re
import sys
import os

def usage():  
    print("%s <A_file> <B_file> <C_file>" %sys.argv[0]);  

#判断A文本中的内容在B文本里边，然后读取B文本中拼音，得C
#注意所有文件都应保存成utf-8的文本文件。
 
fa=open(sys.argv[1]).readlines()
fb=open(sys.argv[2]).readlines()
fc=open(sys.argv[3],'w')
k=0
for i in fa:
#    print i
    temp_fa = i.replace('\n','') #去除回车号，以空格分割
#    print 'temp_fa=',temp_fa
    done = 0 #存在标志
    k=k+1
    print k                      #去计数器，显示进度
    for j in fb:
#        print j
        temp_fb = j.replace('\n','').split(' ') #去除回车号，以空格分割
#        print 'temp_fb[0]=',temp_fb[0],'temp_fb[1]=',temp_fb[1],'\n',  #打印检查分割效果
#        print 'temp_fa=',temp_fa,'temp_fb[1]=',temp_fb[1],'\n',        #打印检查AB文件项目
        if temp_fa == temp_fb[1]: #如果A文件项目存在于B文件里
#            print 'GOOD=',temp_fb,'\n',
#        print 'temp_fb[1]=',temp_fb[1],'\n',                           #打印检查B文件项目
            fc.write(''.join(j)) #带拼音写入C文件
            done = 1 #存在标志
    if done==0:
        fc.write(''.join(i)) #无拼音保持原样写入C文件
#fc.close()
