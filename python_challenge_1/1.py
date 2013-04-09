'''1.py
@author: cnfuyu
@date:2013-3-23
'''

import string

def solve1(s):
    out = ''
    for x in s:
        if ord(x) >= ord('a') and ord(x) <= ord('z'):
            out += chr((ord(x) + 2 - ord('a')) % 26 + ord('a'))
        else:
    	    out += x
    return out

def solve2(s):
    out = ''.join([chr((ord(x) + 2 - ord('a')) % 26 + ord('a')) for x in s])
    return out

def solve3(s):
    table = string.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmnopqrstuvwxyzab')
    out = s.translate(table)
    return out

def solve4(s):
    table = string.maketrans(string.lowercase, string.lowercase[2:] + string.lowercase[:2])
    out = s.translate(table)
    return out

def solve5(s):
     dic = dict(zip(string.lowercase, string.lowercase[2:] + string.lowercase[:2]))
     out = ''.join([dic.get(x, x) for x in s])
     return out
 
if __name__ == '__main__':
    print solve1('mapz;')
    print solve2('mapz;')
    print solve3('mapz;')
    print solve4('mapz;')
    print solve5('mapz;')
