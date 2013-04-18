#!usr/bin/env python
#-*- coding: utf-8 -*-

'''17.py
@author:cnfuyu
@date:2013-4-18
'''

import urllib, re
from urllib2 import Request, urlopen
from urllib import quote_plus

def solve(prefix, nid):
    regex = re.compile(r'busynothing is (\d+)').search
    info = ''
    while True:
        req = urllib.urlopen(prefix + nid)
        text = req.read()
        print text
        nextid = regex(text)
        cookies = req.info().getheaders('set-Cookie')[0]
        byte = cookies.split(';')[0].split('=')[1]
        info += byte
        if nextid:
            nid = nextid.group(1)
            print nid
        else:
            break
    print urllib.unquote_plus(info).decode('bz2')

if __name__ == '__main__':
    prefix = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='
    nothing = '12345'
    #nothing = '8022'
    solve(prefix, nothing)
    info = 'the flowers are on their way'
    url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'
    req = Request(url, headers={'Cookie' : 'info=' + quote_plus(info)})
    print urlopen(req).read()
