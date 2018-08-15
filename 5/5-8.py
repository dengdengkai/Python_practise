#!/usr/bin/python
#coding: UTF-8
"""
封装一个数字比较函数，并比较输入数字:
"""
def compare(num1,num2):
    if num1 > num2:
        print '%s大于%s' % (num1,num2)
    elif num1 < num2:
        print '%s小于%s' % (num1,num2)
    else:
        print '%s等于%s' % (num1,num2)
if __name__ == '__main__':
    numOne = input("请输入第一个数字：")

    numTwo = input("请输入第二个数字：")
    compare(numOne,numTwo)
