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

JJM={}   #精简码专用字典
LQM={}   #六全码专用字典
BSM={}   #笔顺码专用字典
JJM_PPP={}   #精简码字频专用字典
LQM_PPP={}   #六全码字频专用字典
BSM_PPP={}   #笔顺码字频专用字典

for x in fa:
    xx = x.replace('\n','').split('\t') #去除回车号，以制表符分割
#    print xx[1],xx[3],xx[5],xx[7]             #测试显示提取汉字、精简码、六全码、笔顺码
    text=unicode(xx[1],'utf-8')         #先转码再放入字典，否则查询不出
    JJM[text]=xx[3]
    LQM[text]=xx[5]
    BSM[text]=xx[7]
    JJM_PPP[text]=xx[4]
    LQM_PPP[text]=xx[6]
    BSM_PPP[text]=xx[8]
#print LQM                              #测试显示字典结果

for i in fb:
#    print i
    temp = i.replace('\n','').split('\t') #去除回车号，以制表符分割
    text=unicode(temp[1],'utf-8')
    add_JJM=(JJM.get(text))
    add_LQM=(LQM.get(text))
    add_BSM=(BSM.get(text))
    add_JJM_PPP=(JJM_PPP.get(text))
    add_LQM_PPP=1000-int(LQM_PPP.get(text)) #字频改为升序排列
    add_BSM_PPP=1000-int(BSM_PPP.get(text))
    if add_JJM == "null":
        w=temp[1]+'\t'+add_LQM+'\t'+bytes(add_LQM_PPP)+'\n'+temp[1]+'\t'+add_BSM+'\t'+bytes(add_BSM_PPP)+'\n'             #串联格式：字、六全码、笔顺码
    else:
        add_JJM_P=1000-int(add_JJM_PPP)
        w=temp[1]+'\t'+add_JJM+'\t'+bytes(add_JJM_P)+'\n'+temp[1]+'\t'+add_LQM+'\t'+bytes(add_LQM_PPP)+'\n'+temp[1]+'\t'+add_BSM+'\t'+bytes(add_BSM_PPP)+'\n'   #串联格式：字、精简码、六全码、笔顺码
    fc.write(''.join(w))                           #写入C文件

#fc.close()
