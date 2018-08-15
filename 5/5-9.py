#!/usr/bin/python
#coding: UTF-8
"""
题目：使用lambda来创建匿名函数。
程序分析：无
"""
MAXINUM = lambda x,y : ( x > y ) * x + ( x < y ) * y
MININUM = lambda x,y : ( x > y ) * y +( x < y ) * x
a = 10
b = 20 
print 'The largar one is %d' % MAXINUM(a,b)
print 'The lower one is %d' % MININUM(a,b)
