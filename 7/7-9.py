#coding: UTF-8

#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
程序分析：pop(0)表示弹出下标为0的数。将不是3的下标倍数的值插入列表末尾，下标是三的倍数的值的直接弹出
"""
data = [i+1 for i in range(20)]
print(data)
i = 1
while len(data) > 1:
    if i % 3 ==0:
        data.pop(0)
        print data
    else:
        data.insert(len(data),data.pop(0))
        print data
    i += 1
print(data)     
