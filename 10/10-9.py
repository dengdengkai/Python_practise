#束!/usr/bin/python
#coding: UTF-8
"""
题目：有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中。
程序分析：无。
"""
import string
fp = open('test1.txt')
a = fp.read()
fp.close()

fp = open('test2.txt')
b =fp.read()
fp.close()

fp = open('test3.txt','a')
l = list(a+b)
l.sort()
s = ''
s = s.join(l)
fp.write(s)
fp.close()

#运行以上程序前，你需要在脚本执行的目录下创建 test1.txt、test2.txt 文件
