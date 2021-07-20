# coding=utf8

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

# month_number = 0
# while month_number not in range(1,12):
try:
    month_number = int(input('Введите номер месяца: '))
    if month_number not in range(1,13):
        raise ValueError('Значение должно быть от 1 до 12')
except ValueError as err_str:
        print(err_str)
else:
    year_list = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
    year_dict = {1:'Зима', 2:'Зима', 3:'Весна', 4:'Весна', 5:'Весна', 6:'Лето', 7:'Лето', 8:'Лето', 9:'Осень', 10:'Осень', 11:'Осень', 12:'Зима'}
    print(f'Решение списком: {year_list[month_number-1]}')
    print(f'Решение словарем: {year_dict[month_number]}')
