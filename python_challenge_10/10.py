#!usr/bin/env python
# -*- coding:utf-8 -*-

'''10.py
@author:cnfuyu
@date:2013-4-2
'''

import re

if __name__ == '__main__':
    regex = re.compile(r'(\d)(\1*)')
    a = '1'
    for t in range(30):
        a = "".join([str(len(i + j)) + i for i, j  in regex.findall(a)])
    print len(a)
