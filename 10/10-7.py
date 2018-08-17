#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
题目：从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个 # 为止。
程序分析：无。
"""
from sys import stdout
filename = raw_input('输入文件名：\n')
fp = open(filename,"w")
ch =raw_input("输入字符串：\n")
while ch != '#':
    fp.write(ch)
    stdout.write(ch)
    ch = raw_input('')
fp.close()

#实例中创建了 runoobfile.txt 文件并向其写入 runoob 和 google 两个字符串，查看 runoobfile.txt 文件内容：
#输入‘#’结束
