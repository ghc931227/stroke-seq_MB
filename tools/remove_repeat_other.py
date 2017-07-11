#!/usr/bin/env python  
#-*- coding: UTF-8 -*-
import sys;  
#删除第二个（想增加的）文件中与第一个（已经有的）文件相同的行，放入第三个文件

def usage():  
    print("%s <1_file> <2_file> <3_file>" %sys.argv[0]);  

#判断B的内容不在A里面就可以写入C
 
fa=open(sys.argv[1]).readlines()
fb=open(sys.argv[2]).readlines()
fc=open(sys.argv[3],'w')
fc.write(''.join(i for i in fb if i not in fa))
fc.close()

