#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''18.py
@author:cnfuyu
@date:2013-4-26
'''

import difflib

if __name__ =='__main__':
    deltas = open('deltas').read()
    left, right, png = [], [], ['', '', '']

    for row in deltas.splitlines():
        left.append(row[:53])
        right.append(row[56:])
    
    diff = difflib.ndiff(left, right)
    
    for row in diff:
        nst = [chr(int(st, 16)) for st in row[2:].split()]
        if row[0] == '-' : png[0] += ''.join(nst)
        elif row[0] == '+' : png[1] += ''.join(nst)
        elif row[0] == ' ' : png[2] += ''.join(nst)

    for i in range(3):
        open('./python_challenge_18_%d' % i, 'w').write(png[i])
