#!/usr/nin/python
#coding: UTF-8
"""
题目：某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
程序分析：无。
"""
n =int(raw_input("请输入一个四位数数："))

while n <1000 or n > 9999:
      n =int(raw_input("请输入一个四位数数："))
n =str(n)
a = []
for i in range(4):
    a.append((int(n[i])+5)%10)
a[0],a[3] =a[3],a[0]
a[1],a[2] = a[2],a[1]
print "".join('%s' %s for s in a)
