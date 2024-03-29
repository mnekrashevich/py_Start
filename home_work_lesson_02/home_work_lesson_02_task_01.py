# coding=utf8

"""
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

# Заполняем список чем попало:
new_list = [True, 1, 1, 2.5, True, False, 'String',[1, 2, 4], (2, 5, 6), {4:3,5:6}, None]
# Перебираем список по for in
print('Решение задачи:')
for i in new_list:
    print(f'{i}    -    {type(i)}')


# Вроде все работает и задача решена, но хотелось бы пронумеровать(дополнительно вывести индексы элемента списка)
# и тут мы обнаруживаем, что сделать этого через for in нельзя, так как при таком переборе, через переменную итератор
# мы получаем доступ к значению элемента списка, никак не связанное с позицией этого элемента в списке.

# можно было бы попробовать сделать так:
print('Попытка пронумеровать:')
for i in new_list:
    print(f'{new_list.index(i)} : {i}    -    {type(i)}')
# но по значению мы получаем индекс первого вхождение(не то, что нам надо)
# по этому, либо приделываем в цикл доп.переменную
print('Нумеруем через переменную:')
n = 0
for i in new_list:
    print(f'{n} : {i}    -    {type(i)}')
    n += 1
# Либо перебираем список по индексам
print('Перебираем по индексам:')
for i in range(0,len(new_list)):
    print(f'{i} : {new_list[i]}    -    {type(new_list[i])}')

#Или через нумератор
print('enumerate:')
for ind, el in enumerate(new_list):
    print(ind, el)




# Попутно выяснилось: при получении индекса списка по значению элемента результат не совсем очевиден
# Видимо Питон не видит ваобще никакой разницы между True и 1, False и 0.
# Непонятно это баг или фича
# Если в операциях сравнения в этом есть какая то логика - преобразование сравниваемых значений ко одному типу,
# то в данном случае это ближе к багу чем к фиче.

tmp_list = [0, 1, False, True]
print(tmp_list.index(False)) #хотим индекс 2 получаем 0
print(tmp_list.index(True))  #хотим индекс 3 получаем 1

tmp_list = [False, True, 0, 1]
print(tmp_list.index(0))    #хотим индекс 2 получаем 0
print(tmp_list.index(1))    #хотим индекс 3 получаем 1
