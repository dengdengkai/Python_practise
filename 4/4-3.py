#!/usr/bin/python
#coding: UTF-8
"""
按逗号分割列表
"""
l = [1,2,3,4,5,6,7,8,9]
o = '';
for i in l:
    o +=str(i)+','
print o
print (o[0:-1]) #显示0-倒数第二个字符 
