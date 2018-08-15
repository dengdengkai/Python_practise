#!/usr/bin/python
# coding:UTF-8


"""

题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
程序分析：无。
"""


def desc_output(s):
    if(len(s) > 0):
        print(s[-1])
        desc_output(s[0:-1])
s = raw_input("input a string:  ")
desc_output(s)
