#!/usr/bin/python
#coding: UTF-8
"""
娱乐一下
"""
import time
if __name__ =='__main__':
     date=time.strftime('%m-%d',time.localtime())
     if date == '07-07' or  date =='02-14':
         print '情人节是时候给你女朋友买支玫瑰花了！'
     else:
         print "这时候不要忘记发个红包哈！"
     print '哈哈，这是一个测试题！'
