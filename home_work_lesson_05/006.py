# coding=utf8

# Будем считать что формат файла предполагает что:
# в каждой строке файла содержится информация об одном предмете
# название предмета начинает строку и продолжается до знака ":" или до конца строки
# далее в строке есть описание количества часов по предмету,
# перед количеством стоит пробел а после "(" за которой следует сокращенное наименование вида работ по предмету

import re

filename = '006.txt'
mode = 'r'
with open(filename, mode, encoding='utf-8') as file:
    my_dict = {}
    for i_str in file.readlines():
        name = re.match('[^\:]*',i_str)[0]
        hours = sum([float(el) for el in re.findall('(?<=\s)\d*\.?\d(?=\()',i_str)])
        my_dict[name] = hours
    print(my_dict)


