#!/usr/bin/python
# -*- coding: utf-8 -*-
# 本程序用于检查新文件里的每个汉字是否已经存在于旧文件中，该汉字如果不存在就输出保存为待添加文件。

import sys                        #导入系统信息模块
#import struct                                            #导入字符串模块
#import pdb                                               #导入调试模块
#import re                                                #导入正则表达式模块
#import os                                                #导入系统调用模块


#print len(sys.argv) #打印检查命令参数个数
if len(sys.argv)<4:                #如果参数太少
    print "参数太少，请在运行的程序后输入三个参数：新文件、旧文件、输出文件"
elif len(sys.argv)>4:              #如果参数太多
    print "参数太多，请在运行的程序后输入三个参数：新文件、旧文件、输出文件"
elif len(sys.argv)==4:             #如果参数足够
    print "程序名：",sys.argv[0], "新文件：",sys.argv[1], "旧文件：",sys.argv[2], "输出文件：",sys.argv[3]   #打印检查新旧文件名称是否正确


f_old=open(sys.argv[2],'r')         #打开旧文件
line_old=f_old.readlines()          #读取文件全部内容 
#print line_old[2],                                         #打印检查某一行
#print "总共有",len(sys.argv),"行"                           #打印检查旧文件行数
oldfile_lines=len(sys.argv)         #变量赋值旧文件行数
output=sys.stdout                   #重定向输出，用于显示运行进度百分比
old_text=[]                         #用于存放旧文件的汉字列表
for old_line in line_old:           #对旧文件的每一行操作
#    print old_line,                                        #打印检查这一行
    temp = old_line.replace('\n','').split('\t')  #去除回车号，以Tab制表符分割
#    del(temp[0])                                           #删除无用的信息
    old_text.append(temp[1])        #把有用信息添加进旧文件的汉字列表
#### 注意：所读取的文件的最后一行不能有空行，否则会报错 IndexError: list index out of range
    output.write('\r 旧文件已读取：%.0f%%' %oldfile_lines)   #计算运行进度百分比
    output.flush()                  #显示运行进度百分比
#print old_text[5]                                          #打印检查某一行是否提取了汉字
f_old.close()                       #关闭旧文件
#for i in old_text:                                         #循环打印检查旧文件的汉字列表
#    print i,


f_dif=open(sys.argv[3],'a')          #打开输出文件
f_new=open(sys.argv[1],'r')          #打开新文件
#print "总共有",len(sys.argv),"行"                           #打印检查新文件行数
newfile_lines=len(sys.argv)          #变量赋值新文件行数
output=sys.stdout                    #重定向输出，用于显示运行进度百分比
for new_line in f_new.readlines():   #对新文件的每一行操作
#    print new_line                                          #打印检查这一行
    str_new=new_line.split(" ")[0]   #用空格分割这一行，提取第一个字
#    print str_new                                           #打印检查这一行的第一个字
    if str_new not in old_text:      #如果新文件这个字不存在于旧文件内
#        print new_line.split(" ")[0],'不存在于',sys.argv[2]  #打印检查显示这个字
        f_dif.write(str_new +'\n')    #把这个字写入输出文件一字一行
    output.write('\r 新旧文件已比较：%.0f%%' %newfile_lines)  #计算运行进度百分比
    output.flush()                    #显示运行进度百分比

f_new.close()                         #关闭新文件
f_dif.close()                         #关闭输出文件


#f_dif=open(sys.argv[3],'r')                                 #打开输出文件，作最后检查
#for dif_line in f_dif.readlines():                          #对输出文件的每一行操作
#    print dif_line,                                         #循环打印检查输出文件的汉字列表
#f_dif.close()                                               #关闭输出文件


