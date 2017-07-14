#!/usr/bin/env python  
#-*- coding: UTF-8 -*-


import os
import sys;
import codecs;
reload(sys)
sys.setdefaultencoding("utf-8")

def usage():  
    print("%s <A_file> <B_file> <C_file>" %sys.argv[0]);  

#判断A文本中的内容在B文本里边，然后读取B文本中拼音，得C
#注意所有文件都应保存成utf-8的文本文件，末尾不要留空行。
 
fa=open(sys.argv[1]).readlines()
fb=open(sys.argv[2]).readlines()
fc=open(sys.argv[3],'w')

PY={}   #拼音专用字典

for x in fb:
    xx = x.replace('\n','').split('\t') #去除回车号，以制表符分割
#    print xx[0],xx[1]             #测试显示提取拼音、汉字
    text=unicode(xx[1],'utf-8')         #先转码再放入字典，否则查询不出
    PY[text]=xx[0]
#print PY                              #测试显示字典结果

for i in fa:
#    print i
    temp_fa = i.replace('\n','').split('\t') #去除回车号，以制表符分割
#    print 'temp_fa=',temp_fa
    tt=unicode(temp_fa[0],'utf-8')
#    print LQM.get(tt)                          #测试显示单字在字典中的查询结果，无编码则为None
    add_PY=str(PY.get(tt))+"\t"+tt+"\n"
    fc.write(''.join(add_PY))                           #写入C文件
    continue

#fc.close()
