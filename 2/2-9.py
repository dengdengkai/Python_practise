#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
"""
Sn = []
for i in range(2,1001):
    for j in range(1,i):
        if i % j == 0:
           Sn.append(j)
    if i==reduce(lambda x,y : x+y,Sn):
        print i,Sn
    Sn = []
