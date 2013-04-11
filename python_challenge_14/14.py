#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''14.py
@author:cnfuyu
@date:2013-4-11
'''

import Image

if __name__ == '__main__':
    im = Image.open('./python_challenge_14.png')
    nim = Image.new(im.mode, (100, 100))
    left, bottom, right, top = 0, 0, 99, 99
    x, y = 0, 0
    dirx, diry = 0, 1
    
    for t in range(10000):
        nim.putpixel( (x, y), im.getpixel( (t, 0) ) )
        if x == left and y == top:
            dirx, diry = 1, 0
        elif x == right and y == top:
            dirx, diry = 0, -1
        elif x == right and y == bottom:
            dirx, diry = -1, 0
        elif x == left + 1 and y == bottom:
            dirx, diry = 0, 1
            left += 1
            right -= 1
            top -= 1
            bottom += 1

        x += dirx
        y += diry
    
    nim.save('./python_challenge_result_14.png')

