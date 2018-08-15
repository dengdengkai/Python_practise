#!/usr/bin/python
#coding: UTF-8
"""
题目：将一个数组逆序输出。
程序分析：用第一个与最后一个交换。
"""
if __name__ == '__main__':
#方法2
    a = [9,6,5,4,1]
    print a[::-1]
a = [9,6,5,4,1]
#方法1
b=[]
for i in range(len(a)):
    if len(a) > 0:
         b.append(a.pop())
print b 


