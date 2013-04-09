#!usr/bin/env python
#-*- coding:utf-8 -*-

'''12.py
@author:cnfuyu
@date:2013-4-7
'''

if __name__ == '__main__':
    data = open('./evil2.gfx', 'rb').read()

    for i in range(5):
        f = open('./python_challenge_11/%d' % i, 'wb')
        f.write(data[i::5])
        f.close()
