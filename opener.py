# -*- coding: utf-8 -*-
#!usr/bin/python3

"""Опенинг моего ступид яп"""

from syntax import syntax

__version__ = '0.1.8'

commad_file = []

print(f'SourceScript версии: {__version__}')

def read_code(file):
	try:
		with open(file, 'r', encoding='utf-8') as tfile:
			syntax(tfile)


	except Exception as e:
		print('Не вижу данного файла')
		print(e)

