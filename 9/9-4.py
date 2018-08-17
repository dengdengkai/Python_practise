#!/usr/bin/python
#coding: UTF-8
"""
题目：输入一个奇数，然后判断最少几个 9 除以该数的结果为整数。
程序分析：999999 / 13 = 76923。
"""
sum = 9
i = int(raw_input('input a number:'))
while sum % i != 0:
     sum = sum * 10 + 9
print '%s个9可以整除' % len(str(sum)),sum
