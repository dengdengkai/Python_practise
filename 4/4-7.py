#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
题目：对10个数进行排序。
程序分析：可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。
"""
print '请输入10个数字'
L = []
for i  in range(1,11):
    print '请输入第%d个数字' % i
    n = int(raw_input())
    L.append(n)

L.sort()
print  '排序后的数字', L

