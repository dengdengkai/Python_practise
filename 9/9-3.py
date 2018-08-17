#!/usr/bin/python
#coding: UTF-8
"""
题目：求0—7所能组成的奇数个数。
程序分析：
组成1位数是4个。
组成2位数是7*4个。
组成3位数是7*8*4个。
组成4位数是7*8*8*4个。
#0-7最多组为8位数，最少为1位数
"""
sum = 4 #所有位数奇数和
s = 4   #第一位总奇数
print '1位数情况',s           
for i in range(2,9):  #模拟2到8位数的情况
    if i ==2:
        s *=7  #第2位总奇数
    else:
        s *=8  #第i位总奇数
    sum += s  # 第i位总奇数及前i位奇数数量和
    print '%d位数情况' % i,s
print 'sum = %d'  % sum
       

