#!/usr/bin/python
#coding: UTF-8
"""
题目：输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
程序分析：无。
"""
a = [1,2,3,7,9,8]
print "原列表：%s" % a
min = min(a)
a.remove(min)
a.append(min)

max=max(a)
a.remove(max)
a.insert(0,max)
print "新列表：%s" % a
