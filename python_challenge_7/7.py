#!usr/bin/env python
# -*- coding:utf-8 -*-

'''7.py
@author:cnfuyu
@date:2013-3-31
'''

from PIL import Image

if __name__ == '__main__':
    im = Image.open('./python_challenge_7.png')
    h = im.size[1] / 2
    pix = [im.getpixel((x, h)) for x in range(0, im.size[0], 7)]
    print ''.join([chr(r) for r, g, b, a in pix])
    data = [105, 110, 116, 101, 103, 114, 105, 116, 121]
    print ''.join([chr(x) for x in data])
