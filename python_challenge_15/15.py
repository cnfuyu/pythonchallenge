#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''15.py
@author:cnfuyu
@date:2013-4-11
'''

import calendar

if __name__ == '__main__':
    for x in range(100):
        year = 1006 + x * 10
        if calendar.weekday(year, 1, 1) == 3 and calendar.isleap(year) == True:
            print year
