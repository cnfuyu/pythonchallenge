#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''13.py
@author:cnfuyu
@date:2013-4-11
'''

from xmlrpclib import ServerProxy

if __name__ == '__main__':
    http = 'http://www.pythonchallenge.com/pc/phonebook.php'
    server = ServerProxy(http)
    print server.system.listMethods()
    #Bert is evil
    print server.phone('Bert')
