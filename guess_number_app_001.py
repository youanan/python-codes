#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-11-22 20:50:15
# @Author  : youanan (youanan@163.com)
"""
猜数值小游戏，内定一个数值，不断提示用户输入数值，
不断提示用户输入的数值比较，完全正确后，提示一真猜了多少次
"""

#内定一个数值
number = 59
#猜的次数
gno = 0
#定义一个假值变量
guess_flag = False

#当变量为真是一直循环
while guess_flag == False:
    #循环请用户输入数值
    guess = int(input('Enter on integer: '))
    #如果数值与内定数值相同
    if guess == number:
        #改变变量值为真
        guess_flag = True
        #如果数值小于内定数值
    elif guess < number:
        print u'不对，数字太小了，继续猜...'
        gno += 1
        #如果不小于、不等于
    else:
        gno += 1
        print u'不对，数字太大了，继续猜...'

print u'恭喜你，猜对了!'
print u'你一共猜了%s次!' %gno
print u'Done!'