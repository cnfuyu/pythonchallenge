#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''3.py
@author:cnfuyu
@date:2013-3-24
'''

import re

def solve1(filename):
    data = open(filename).read()
    m = ''.join(ch[4] for ch in re.findall(r'[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]', data))
    print m

if __name__ == '__main__':
    filename = 'equality.txt'
    solve1(filename)
