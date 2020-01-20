#!/usr/bin/env python  
#-*- coding: UTF-8 -*-

import os
import sys;
import codecs;
reload(sys)
sys.setdefaultencoding("utf-8")

def usage():  
    print("%s <A_file> <B_file> <C_file>" %sys.argv[0]);  

#用于排除原词库已有的字词，或者黑名单。用python字典的方式，速度特快，适合百万千万以上级别的词库比较。
#从第二个文件里的提取词组，与第一个文件的提取的关键字（字典）比较，如果不重复，则写入C文件。
#注意所有文件都应保存成utf-8的文本文件，末尾不要有空行。
 
fa=open(sys.argv[1]).readlines()
fb=open(sys.argv[2]).readlines()
fc=open(sys.argv[3],'w')

LQM={}                                    #黑名单专用字典

for x in fa:
    xx = x.replace('\n','').split('\t')   #去除回车号，以制表符分割
#    print xx[1],xx[5],xx[7]              #测试显示提取汉字、六全码、笔顺码
    text=unicode(xx[0],'utf-8')           #先转码再放入字典，否则查询不出
    LQM[text]=xx[0]
#print "xx=",xx,"text=",text,"dd=",LQM    #测试显示字典结果


for i in fb:
#    print i
    temp = i.replace('\n','').split('\t') #去除回车号，以制表符分割
    text=unicode(temp[1],'utf-8')
    if text not in LQM:
       w=i                                #这里可以调整格式
       fc.write(''.join(w))               #写入C文件
#fc.close()
