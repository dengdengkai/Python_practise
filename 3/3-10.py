#!/usr/bin/python
# coding: UTF-8
"""
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
程序分析：无。
"""
a = input("请输入一个数字")
a  = str(a)
m=a[::-1]
if m == a:
    print '%s是回文数' % a
else:
    print '%s不是回文数' % a
