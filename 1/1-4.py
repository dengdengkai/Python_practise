 #!/usr/bin/python                               
 # -*- coding: UTF-8 -*-
"""

题目：输入某年某月某日，判断这一天是这一年的第几天？
程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
"""

import time 
import sys
reload(sys)

sys.setdefaultencoding('utf-8')
a = raw_input("输入时间（格式如: 2017-04-04）:")
t = time.strptime(a,"%Y-%m-%d")
print time.strftime("今年的第%j天",t).decode('utf-8')
