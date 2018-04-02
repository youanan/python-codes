#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
[in]  checkio([1,2,3,1,3])
[out] [1,3,1,3]
[in]  checkio([1,2,3,4,5])
[out] []
[in]  checkio([10,9,10,10,9,8])
[out] [10,9,10,10,9]
'''
def checkio(mylist):
    lastlist = []
    for i in mylist:
        if mylist.count(i) > 1:
            lastlist.append(i)
    return lastlist

if __name__ == '__main__':
    mylist = raw_input('Please input a number list >>')
    print checkio(mylist)

