#/usr/bin/python
#coding: UTF-8
"""
题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
程序分析：无。
"""
a = []
n = input('你想输入几位数：')
for i in range(1,n+1):
    s = input("请输入第%d位数："%i)
    a.append(s)
m=input("你想将列表移动几位：")
print '排序前的列表：%s'% a
b=a[-m:] #获取后面的m个数
c =a[:-m] #获取前面除了m的数
a = b+c
print '排序后列表：%s'%a
