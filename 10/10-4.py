#!/usr/bin/python
#coding: UTF-8
"""
题目：时间函数举例4,一个猜数游戏，判断一个人反应快慢。
程序分析：无。
"""
import time 
import random
start =time.time()
while True:
    play = raw_input('play the game(Y/n)?')
    if play == 'Y' or play=='y':
        number = random.randint(0,5)
        guess = int(raw_input('guess a number(0-5):'))
        while True:
            if number > guess:
                guess = int(raw_input("guess a bigger number:"))
            elif number < guess:
                guess = int(raw_input("guess a smaller number: "))
            else:
                end = time.time()
                print "bingo!"
                print u"%0.2fs猜中" % (end - start)
                break
    else:
        break

