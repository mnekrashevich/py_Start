# coding=utf8

# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(x, y):
    """
    :param x: действительное положительное число
    :param y: целое отрицательное число
    :return: возведение числа x в степень y
    """
    err_msg = ''
    err = False
    if not isinstance(x, (type(float(0)), type(int(0)))) or x <= 0:
        err_msg += 'Первое число должно быть действительным положительным. '
        err = True
    if not isinstance(y, type(int(0))) or y >= 0:
        err_msg += 'Второе число должно быть целым отрицательным.'
        err = True
    if err:
        print(err_msg)
        return
    result = 1
    for i in range(-y):
        result /= x
    print(f'Проверка {x**y}')
    return result

print(my_func(1,5))
print(my_func(1.4,5))
print(my_func('asdf',5))
print(my_func(1,5))
print(my_func(1,5))
print(my_func(2,-5))
print(my_func(1.567,-9.56))
print(my_func(1.567,-9))
