#!/usr/bin/env python  
#-*- coding: UTF-8 -*-
#本程序用于修正词库中错误的单字编码，替换为正确的编码。

import os
import sys;
import codecs;
reload(sys)
sys.setdefaultencoding("utf-8")

def usage():  
    print("%s <A_file> <B_file>" %sys.argv[0]);  

#按第一个文件的单字和编码查找，在第二个文件里的词组中分割汉字，如果符合就替换（小心，如果程序错误，第二个文件会被清空）。
#注意所有文件都应保存成utf-8的文本文件，末尾不要有空行。

import re
fa=open(sys.argv[1]).readlines()
for x in fa:
    xx = x.replace('\n','').split('\t')       #去除回车号，以制表符分割
#    print xx[0],xx[1],xx[2]                   #测试显示提取汉字、正确的六全码、正确的笔顺码
    text_a=unicode(xx[0],'utf-8')             #第一个文件的单字，先转码，否则查询不出
#    print "text_a=",text_a

#分析：第二个文件先以只读模式打开后，对文件每一行进行readlines()操作，并保存到新的列表中。然后随之关闭。
#再次以'w+'方式进行读写打开第二个文件，并用f.writelines()函数写入第二个文件。

    fb=open(sys.argv[2],'r')
    all_fb_lines=fb.readlines()
    fb.close()
    fc=open(sys.argv[2],'w')
    for i in all_fb_lines:
#        print i
        w=""
        temp = i.replace('\n','').split('\t')  #这一行去除回车号，以制表符分割
#        for ii in temp:
#            print ii                          #测试显示分组结果
        LQM = ""
        BSM = ""
        temp_LQM = temp[2].replace('\n','').split('.')      #词组可能错误的六全码,去除回车号，以点号分割
        temp_BSM = temp[3].replace('\n','').split('.')      #词组可能错误的笔顺码,去除回车号，以点号分割
        text_b=unicode(temp[1],'utf-8')                     #第二个文件可能是词组，也可能是单字，先转码，否则查询不出

        fix_ok=0                            #是否被修改过的专用标记
        for j,jj in enumerate(text_b):          #分割词组中的每个单字，j是列表索引，jj是元素
            if jj==text_a:                      #如果词组中的这个字与第一个文件的单字匹配
#                print j,jj                      #测试显示该字
#                print "text_b=",text_b          #测试显示该词组
#                print "wrong_LQM=",temp[2],'\n',"wrong_BSM=",temp[3]      #测试显示该词组所在的行
#                print temp[1],'\t',temp[2],'\t',temp[3]

                for k,kk in enumerate(temp_LQM): #重新组合词组的正确六全码，k是列表索引，kk是元素
                    if k==j:                     #字和编码的索引是否相等
                        temp_LQM[k] = xx[1]      #替换为正确的编码
#                        print "temp_LQM[k]=",temp_LQM
                right_LQM=".".join(temp_LQM)     #整合为正确的词组编码
#                print "right_LQM=",right_LQM

                for m,mm in enumerate(temp_BSM): #重新组合词组的正确笔顺码，m是列表索引，mm是元素
                    if m==j:                     #字和编码的索引是否相等
                        temp_BSM[m] = xx[2]      #替换为正确的编码
#                        print "temp_BSM[m]=",temp_BSM
                right_BSM=".".join(temp_BSM)     #整合为正确的词组编码
#                print "right_BSM=",right_BSM

#                w=temp[0]+'\t'+temp[1]+'\t'+right_LQM+'\n'+temp[1]+'\t'+right_BSM+'\n'  #分两行串联格式：词组、六全码、笔顺码
                w=temp[0]+'\t'+temp[1]+'\t'+right_LQM+'\t'+right_BSM+'\n'               #同一行串联格式：词组、六全码、笔顺码
#                print w
                fix_ok=1                        #标记被修改过
        if fix_ok==0:
            w=i                                 #如果未被修改过，则照搬
        fc.write(''.join(w))                    #写入第二个文件
    fc.close()
