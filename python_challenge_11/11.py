#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''11.py
@author:cnfuyu
@date:2013-4-6
'''

import Image, ImageDraw

if __name__ == '__main__':
    im = Image.open('./python_challenge_11.jpg')
    nim = Image.new(im.mode, (im.size[0] / 2, im.size[1] / 2) )
    
    for x in range(1, im.size[0], 2):
        for y in range(1, im.size[1], 2):
            nim.putpixel( (x // 2, y // 2), im.getpixel( (x, y) ) ) 

    nim.save('./python_challenge_11_result.png')
