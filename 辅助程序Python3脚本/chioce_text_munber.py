#-*- coding: UTF-8 -*-
import re
import sys
import os

#判断文本中汉字的那一列内容，汉字是否大于4个，是就删除，剩余得C
 
fa=open(sys.argv[1]).readlines()
fb=open(sys.argv[2],'w')

with open(sys.argv[1], 'rb') as f:
    for line in f:
        temp_fa = line.split(' ') #以空格分割
        #print 'temp_fa[0]=',temp_fa[0],'temp_fa[1]=',temp_fa[1],'\n',  #打印检查分割效果
        if len(temp_fa[1]) < 16 :                                #判断是否小于等于4个
            fb.write(''.join(temp_fa[0]+' '+temp_fa[1]))        #存在则把带拼音的写入新文件



