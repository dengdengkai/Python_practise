#!/usr/bin/python
#coding: UTF-8
"""
题目：求输入数字的平方，如果平方运算后小于 50 则退出。
程序分析：无
"""
while 1:
    n = int(raw_input("请输入一个数字："))
    print '运算结果为：%d' %  (n**2)
    if n**2 < 50:
        quit()
    else:
        print '请继续输入：'
