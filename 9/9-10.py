#!/usr/bin/python
#coding: UTF-8
"""
题目：列表使用实例。
程序分析：无。
"""
#list
#新建列表
testList=[10086,'中国移动',[1,2,4,5]]

#访问列表长度
print len(testList)

#1到列表结尾 不是0
print testList[1:]
testList.append('i\'m new here!')
print len(testList)


#访问最后一个元素
print testList[-1]

#弹出列表的最后一个元素
print testList.pop(1)
print len(testList)
print testList

matrix = [[1, 2, 3],  
[4, 5, 6],  
[7, 8, 9]]  
print matrix  
print matrix[1]  
col2 = [row[1] for row in matrix]#get a  column from a matrix  
print col2  
col2even = [row[1] for row in matrix if  row[1] % 2 == 0]#filter odd item  
print col2even
