"""SourceScript syntax"""

import sys 
import os 
import re
import glob
import time
#import sqlite3

def invalid_syntax():
    print('Ошибка синтаксиса')
    sys.exit()

def error(line):
	w = os.path.abspath(__file__)
	print(f'Ошибка в {w}\n>>>{line}')
	sys.exit()

def numberical():
    print('Не могу добавить строку к цыфре')
    sys.exit()

command = {
    'rprint': 'печатать',
    'exit': 'выход',
    'add': 'добавить',
    'minus': 'вычесть',
    'len': 'длина',
    'get': 'получить',
    'put': 'запись',
    'create': 'создать',
    'wait': 'ждать',
    'for': 'пока',
    'open': 'открить'
} 

def minus(line):
    try:
        txt = re.sub(r"\s", " ", line)
        out_txt = re.split(r"[(),]", txt)
        num1 = out_txt[1]
        num2 = out_txt[2]
        print(int(num1) - int(num2))
    except Exception as e:
        numberical()

def put_def(line):
    txt = re.sub(r"\s", " ", line)
    out_txt = re.split(r"[()]", txt)
    input(out_txt[1])

def _open_whis_file(line, open_file_us, **argument):
		for file_type_of_open,name in argument.items():
			try:
				name = open(open_file_us, str(file_type_of_open))
			except Exception as e:
				print(e)
				error(line)

def open_def(line):
	txt = re.sub(r"\s", " ", line)
	out_txt = re.split(r"[(),]", txt)
	print(out_txt)
	_open_whis_file(line, out_txt[1], file_type_of_open=out_txt[2], name=out_txt[3])





def add(line):
    try:
        txt = re.sub(r"\s", " ", line)
        out_txt = re.split(r"[(),]", txt)
        num1 = out_txt[1]
        num2 = out_txt[2]
        print(int(num1) + int(num2))
    except Exception as e:
        numberical()

def parser_sleep(line):
    txt = re.sub(r"\s", " ", line)
    out_txt = re.split(r"[()]", txt)
    time.sleep(int(out_txt[1]))

def _len_(line):
    txt = re.sub(r"\s", " ", line)
    out_txt = re.split(r"[()]", txt)
    print(len(out_txt[1]))

def rprint(line):
	    txt = re.sub(r"\s", " ", line)
	    out_txt = re.split(r"[()]", txt)
	    print(out_txt[1], end='\n')

def exit(line):
    print(f'\n\n\nВыход из программы')
    sys.exit()

def get_module(main_line):
    get = main_line.split()[1]
    if get == '*':
        get = glob.glob('*.bl')

    else:
        pass

    try:
        with open(f'{get}.bl', 'r', encoding="UTF-8") as lib:
            for line in lib:
                syntax(line)

    except Exception as e:
        print(e)
        print(f'Не вижу {get} модуля(ей), или он пуст!') 

def for_def(line):
	try:
		data = line
		text = line
		txt = re.sub(r"\s", " ", text)
		out_txt = re.split(r"[()]", txt)
		arg = out_txt[1]
		do = re.findall('\{([\s\S]*?)\}', data)
		print(arg)
		if arg == 'True':
			while True:
				syntax(do)

		elif arg == 'False':
			invalid_syntax()

		elif arg == '' or arg == ' ':
			for x in range(1):
				syntax(do)

		else:
			while arg:
				syntax(do)

	except Exception as e:
		print(e)


def syntax(file):
	for line in file:
		if line.startswith('$') != True:
			try:
				try:
					line[0]
				except:
					print('Файл пуст')

				if command['for'] in line:
					for_def(line)

				if command['rprint'] in line:
					rprint(line)

				elif command['exit'] in line:
					exit(line)

				elif command['add'] in line:
					add(line)

				elif command['minus'] in line:
					minus(line)

				elif command['len'] in line:
					_len_(line)

				elif command['get'] in line:
					get_module(line)

				elif command['get'] in line:
					get_module(line)

				elif command['put'] in line:
					put_def(line)

				elif command['wait'] in line:
					parser_sleep(line)

				elif command['open'] in line:
					open_def(line)

				else:
					if line == '\n':
						pass
					else:
						error(line)

			except Exception as e:
				print(e)