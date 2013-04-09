'''2.py
@author:cnfuyu
@date:2013-3-24
'''

import string

def solve1(filename):
    data = open(filename).read()
    d = {}
    for ch in data:
	d[ch] = d.get(ch, 0) + 1
    print ''.join(ch for ch in data if d[ch] == 1)

def solve2(filename):
    data = open(filename).read()
    print filter(lambda x: x in string.letters, data)

def solve3(filename):
    data = open(filename).read()
    for a in data:
	l = data.count(a)
	if l < 20:
	    print a, ":", l

if __name__ == '__main__':
    filename = 'ocr.txt'
    solve1(filename)
    solve2(filename)
    solve3(filename)
