# coding=utf8

# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(divisible, divisor):
    """
    Функция division(divisible, divisor) принимает в качестве параметров делимое и делитель. Делает попытку
    перобразовать их к float. Возвращает результат деления делимого на делитель. В случае деления на ноль или
    невозможности преобразовать входные данные к числам возвращает строку с описанием ошибки.
    Параметры:
    divisible - Делимое
    divisor - Делитель
    Возвращаемое значение:
    Числовое значение типа float, Строка (в случае ошибки).
    """
    global result
    try:
        divisible_float = float(divisible)
        divisor_float = float(divisor)
        result = divisible_float/divisor_float
    except ZeroDivisionError:
        result = 'Ошибка! Деление на ноль!'
    except Exception:
        result = 'Ошибка! Неверные входные данные!'
    finally:
        return result


for args in [(2, 4), (5, 0), (0, 7), ('asdf', 1), (1, 'asdf'), ('asdf', 'asdf'), ('12', '6'), (True, False), (False, True)]:
    print(division(*args))

print(division(input('Делимое :'), input('Делитель :')))