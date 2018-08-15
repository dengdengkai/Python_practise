#!/usr/bin/python
# coding: UTF-8
"""
题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
程序分析：学会分解出每一位数。
"""
num  = list(raw_input("请输入一个不超过5位数字的数"))
print len(num)
num.reverse()
for i in range(len(num)):
    print num[i],

