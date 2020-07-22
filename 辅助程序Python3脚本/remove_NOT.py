#-*- coding: UTF-8 -*-
import re
import sys
import os

def usage():  
    print("%s <1_file> <2_file> <3_file>" %sys.argv[0]);  

#判断A（黑名单）文本中的内容在B（原始）文本里边然后在B文本中删除得C
#即判断B的内容不在A里面就可以写入C
 
fa=open(sys.argv[1]).readlines()
fb=open(sys.argv[2]).readlines()
fc=open(sys.argv[3],'w')
fc.write(''.join(i for i in fb if i not in fa))
fc.close()


