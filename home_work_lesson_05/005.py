#coding=utf8
import random

filename = '005.txt'
mode = 'w+'
with open(filename, mode, encoding='utf-8') as file:
    file.write(' '.join([str(random.randint(1,5000)) for i in range(random.randint(1,50))]))
    file.seek(0)
    print(sum([int(s) for s in file.read().split()]))
