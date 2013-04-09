#!usr/bin/env python
# -*- coding:utf-8 -*-

'''5.py
@author:cnfuyu
@date:2013-3-27
'''

import pickle

if __name__ == '__main__':
    data = pickle.load(open('banner.p'))
    for line in data:
        print ''.join([c[0] * c[1] for c in line])
