#!/usr/bin/env python  
#-*- coding: UTF-8 -*-

import os
import sys;
import codecs;
reload(sys)
sys.setdefaultencoding("utf-8")

def usage():  
    print("%s <A_file> <B_file> <C_file>" %sys.argv[0]);  

#第二个文件里的词组中分割汉字，按第一个文件的四合一编码，加入六全码和笔顺码，得C文件。
#注意所有文件都应保存成utf-8的文本文件，末尾不要有空行。
 
fa=open(sys.argv[1]).readlines()
fb=open(sys.argv[2]).readlines()
fc=open(sys.argv[3],'w')

LQM={}   #六全码专用字典
BSM={}   #笔顺码专用字典

for x in fa:
    xx = x.replace('\n','').split('\t') #去除回车号，以制表符分割
#    print xx[1],xx[5],xx[7]             #测试显示提取汉字、六全码、笔顺码
    text=unicode(xx[1],'utf-8')         #先转码再放入字典，否则查询不出
    LQM[text]=xx[5]
    BSM[text]=xx[7]
#print LQM                              #测试显示字典结果


for i in fb:
#    print i
    temp = i.replace('\n','').split('\t') #去除回车号，以制表符分割
#    for ii in temp:
#        print ii                          #测试显示分组结果None

    text=unicode(temp[1],'utf-8')
    add_LQM=""                             #用于六全码
    add_BSM=""                             #用于笔顺码
    for j in text:
#        print j                          #测试显示单字结果
#        print LQM.get(j)                          #测试显示单字在字典中的查询结果，无编码则为None
        add_LQM=add_LQM+"."+str(LQM.get(j))
        add_BSM=add_BSM+"."+str(BSM.get(j))
    add_LQM=add_LQM[1:]                            #去除多余的第一个点号
    add_BSM=add_BSM[1:]                            #去除多余的第一个点号
#    print add_LQM,add_BSM                          #测试显示词组编码的结果
    z=i.replace('\n','')                           #原拼音词组去除回车号
    w=z+'\t'+add_LQM+'\t'+add_BSM+'\n'             #串联格式：拼音、词组、六全码、笔顺码
    fc.write(''.join(w))                           #写入C文件

#fc.close()
