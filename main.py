# -*- coding: utf-8 -*-, string
#!usr/bin/python3


"""Главный файл моего ступид яп"""


from opener import *
import sys

name = 'main.bl'

try:
	file = sys.argv[2]
	read_code(file)

except:
	if name == 'None':
		file = input('Enter name of file: ')
		read_code(file)
	else:
		read_code(name)