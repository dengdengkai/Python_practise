#!/usr/bin/python
#-*- coding: UTF-8 -*-
"""

题目：判断101-200之间有多少个素数，并输出所有素数。
程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
"""
import math
l=[]
for x in range(101,200):
    l.append(x)
    for i in range(2,int(math.sqrt(x))+1):
        if x % i ==0:
            l.pop()
            break
n=len(l)
print l
print '总数为：',n
