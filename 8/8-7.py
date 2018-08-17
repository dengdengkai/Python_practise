#!/usr/bin/python
#coding: UTF-8
"""
题目：回答结果（结构体变量传递）。
程序分析：无。
"""
class student:
    x=0
    y=0
def f(stu):
     stu.x=20
     stu.y='c'
a = student()
a.x=3
a.y ='a'
f(a)
print a.x,a.y
