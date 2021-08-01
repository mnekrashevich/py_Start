# coding=utf8
# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
# что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3,
# а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

import itertools
from sys import argv

script_name, *script_param = argv

# script_param = ('--2','14','Попугай','Кеша','Красавчик!')
# script_param = ('--1','5','10')
# script_param = ('--1','50','10')
# script_param = ('--help','50','10')
# script_param = ('-asf','50','10')

my_list = []

if len(script_param) == 0 or script_param[0] == '--help' or script_param[0] not in ('--1','--2'):
    err_msg = '''Скрипт генератор".
    Параметр №1 - Вариант работы скрипта --1 или --2
    --1: Итератор, генерирующий целые числа начиная с указанного в параметре №2 и заканчивающигося параметром №3
    --2: Итератор. повторяющий элементы списка переданного параметрами начиная с 3го столько раз сколько указано
    в параметере №2
    Если первый параметр = "--help" - вывод этой справки.
    '''
    print(err_msg)
elif script_param[0] == '--1':
    start_num = int(script_param[1])
    end_num = int(script_param[2])
    for i in itertools.count(start_num):
        if i <= end_num:
            my_list.append(str(i))
        else:
            break
    print(' '.join(my_list))
elif script_param[0] == '--2':
    gen = itertools.cycle(script_param[2:])
    for i in range(int(script_param[1])):
        my_list.append(next(gen))
    print(' '.join(my_list))












