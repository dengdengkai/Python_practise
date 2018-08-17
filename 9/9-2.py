#/usr/bin/python
#coding: UTF-8
"""
题目：八进制转换为十进制
程序分析：无。
"""

def f8to10(num):
    print '8进制数：%s' % num
    l = num
    length = len(l)
    sum = 0
    for i in range(length):
        sum += 8 ** i * int(l[length-1-i])
    
    return sum
n =str(raw_input("请输入一个八进制数，每一位不能输入8或9："))
x = f8to10(n)
print '转换为10进制数为：', x 

