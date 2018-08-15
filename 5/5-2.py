#!/usr/bin/python
#coding: UTF-8
"""
题目：学习使用auto定义变量的用法。
程序分析：没有auto关键字，使用变量作用域来举例吧。
"""
#验证局部变量（函数内的）与外部变量有无影响
num = 2
def autofunc():
    num = 1
    print 'iinternal block num = %d' % num
    num += 1
for i in range(3):
    print 'The num = %d' % num   #打印外部num的值
    num += 1
    autofunc()  # 调用函数打印内部num的值
