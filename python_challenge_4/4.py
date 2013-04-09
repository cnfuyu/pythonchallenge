#!usr/bin/env python
#-*- coding: utf-8 -*-

'''4.py
@author:cnfuyu
@date:2013-3-26
'''

import urllib, re

def solve1(prefix, nid):
    regex = re.compile(r'nothing is (\d+)').search

    while True:
        text = urllib.urlopen(prefix + nid).read()
	print text
	nextid = regex(text)
        if nextid:
	    nid = nextid.group(1)
	    print nid
	else:
	    break


if __name__ == '__main__':
    prefix = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    #nothing = '12345'
    nothing = '8022'
    solve1(prefix, nothing)

