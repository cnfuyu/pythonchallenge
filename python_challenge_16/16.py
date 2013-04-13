#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''16.py
@author:cnfuyu
@date:2013-4-13
'''

import Image

def make_line_straight(line):
    w = line.index(195)
    return line[w:] + line[:w]

if __name__ == '__main__':
    im = Image.open('./mozart.gif')
    nim = Image.new(im.mode, im.size)

    for y in range(im.size[1]):
        line = [im.getpixel((x, y)) for x in range(im.size[0])]
        line = make_line_straight(line)
        [nim.putpixel((x, y), line[x]) for x in range(im.size[0])]
    
    nim.save('./python_challenge_result_16.gif')
