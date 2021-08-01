# coding=utf8

# 3. Реализовать функцию my_func(), которая принимает
# три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(arg_1, arg_2, arg_3):
    """
    функция принимает три позиционных параметры и возвращает сумму двух наибольших.
    :param arg_1: число
    :param arg_2: число
    :param arg_3: число
    :return: сумма двух наибольщих параметров
    """
    global result
    try:
        param = [arg_1, arg_2, arg_3]
        param.sort()
        result = sum(param[1:])
    except TypeError:
        print('Ошибка. Неверные входные данные')
        result = None
    finally:
        return result


# Test
print(my_func('hgfdxs', 2, 3))
print(my_func([2, 4], [3, 7], [3, 9]))
print(my_func(6, 2, 3))
