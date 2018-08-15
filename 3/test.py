#!/usr/bin/python
#coding:UTF-8

def x(s):
 if len(s)>0:
   print s[-1]
   x(s[0:-1])
a = 'abcdfg'
print a
x(a)



