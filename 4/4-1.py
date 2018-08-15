#!/usr/bin/python
# coding: UTF-8
"""
题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。。
"""
weeklist = {'M':'Monday','T':{'u':'Tuesday','h':'Thursday'},'W':'Wednesday','F':'Friday','S':{'a':'Saturday','u':'Sunday'}}

sletter1 =raw_input("请输入首字母：")
sletter1 = sletter1.upper()

if (sletter1 in ['T','S']):
    sletter2 = raw_input("请输入第二个字母")
    print(weeklist[sletter1][sletter2])
else:
    print(weeklist[sletter1])
