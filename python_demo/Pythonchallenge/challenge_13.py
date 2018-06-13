#!usr/bin/python
# -*- coding:utf-8 -*-

from xmlrpc import client
server = client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
#print(server.system.listMethods())
#print(server.system.methodHelp('phone'))
print(server.phone('Bert'))

