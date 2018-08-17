#!/usr/bin/python
#coding: UTF-8
"""
题目：列表转换为字典。
程序分析：无。
"""
key=['a','b']
value=[1,2]
print dict([key,value])





l1 =[1,2,3,4,5,3]
l2=['aa','bb','cc','dd','ee','gg']
d={}
for index in range(len(l1)):
    d[l1[index]] =l2[index]  ## 注意，key 若重复，则新值覆盖旧值 
print d


# 从列表创建字典
i = ['a','b','c']
l = [1,2,3]
b=dict(zip(i,l))
print(b)
