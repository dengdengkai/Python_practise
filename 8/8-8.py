#!/usr/bin/python
#coding:UTF-8

"""
题目：找到年龄最大的人，并输出。
"""

"""
部分用法解释
调用operator模块中的 itemgetter() 可以实现根据多个参数排序：

>>> sorted(student_tuples, key = itemgetter(2))  # 根据年龄排序
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
>>> sorted(student_tuples, key = itemgetter(1, 2))  # 根据成绩和年龄排序
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
>>> sorted(student_tuples, key = itemgetter(1, 2), reverse=True) # 反转排序结果
[('jane', 'B', 12), ('dave', 'B', 10), ('john', 'A', 15)]
"""
#方法1
import operator
person ={"li":18,"wang":50,"zhang":20,"sun":22}
print max(person.iteritems(),key=operator.itemgetter(1))

print max(person.iteritems(),key=operator.itemgetter(1))[0]
print max(person.values())
