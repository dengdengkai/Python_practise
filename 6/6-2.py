#!/usr/bin/python
# coding: UTF-8
"""
题目：学习使用按位或 | 。
程序分析：0|0=0; 0|1=1; 1|0=1; 1|1=1
"""
if __name__ == '__main__':
    a = 077   #注此处077 =7*8的0次方+7*8的一次方，其中0表示8进制，077不是 77
    b =a | 3
    print 'a | b is %d' % b
    b |= 7
    print 'a | b is %d' % b

