#!usr/bin/env python
# -*- coding:utf-8 -*-

'''6.py
@author:cnfuyu
@date:2013-3-28
'''

import re

if __name__ == '__main__':
   nid  = '90052'
   regex = re.compile(r'nothing is (\d+)').search
   while True:
       match = regex(open('./channel/' + nid  + '.txt').read())
       if match:
           nid = match.group(1)
           print match.group(0), nid
       else:
           print open('./channel/' + nid + '.txt').read()
           break
