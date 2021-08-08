#coding=utf8

filename = 'Задание.txt'
mode = 'r'
with open(filename, mode, encoding='utf-8') as file:
    str_lines = file.readlines()
    print(f'В файле {file.name} - {len(str_lines)} строк(и)')
    for i in enumerate(str_lines, 1):
        print(f'В строке {i[0]} - {len(i[1].split())} слов(а)')