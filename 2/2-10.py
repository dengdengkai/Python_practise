#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
"""
hei = 100.0
tim = 10
height = []
for i in range(2,tim+1):
    hei /=2
    height.append(hei)
print('第10次落地时，反弹%s高'%(min(height)/2.0))
print('第10次落地时，经过%s米'%(sum(height)*2+100))
