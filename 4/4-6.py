#!/usr/bin/python
#coding:UTF-8
"""
求100之内的素数。
"""
lower = int(input("输入区间最小值: "))
upper = int(input("输入区间最大值: "))

for num in range(lower,upper + 1):
    if num > 1:
        flag=0
        for i in range(2,num):
              if num % i == 0:
                   flag = 0
                   break
              else:
                   flag = 1
     
        if flag == 1:
           print(num)




