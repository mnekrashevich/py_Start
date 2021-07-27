# coding=utf8

# 1. Реализовать скрипт, в КОТОРОМ должна быть ПРЕДУСМОТРЕНА функция расчета заработной платы сотрудника. В
# расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для
# конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, *script_param = argv

err_msg = ''
result = 0

if len(script_param) == 0 or script_param[0] == '--help':
    err_msg = '''Скрипт для расчета заработной платы сотрудника по формуле "(выработка в часах * ставка в час) + премия".
    Параметр №1 - Выработка в часах
    Параметр №2 - Ставка в час
    Параметр №3 - Процент премии
    Если первый параметр = "--help" - вывод этой справки. 
    '''
elif len(script_param) != 3:
    err_msg = 'Неверное количество параметров!'
else:
    try:
        production, rate, premium = script_param
        production, rate, premium = float(production), float(rate), float(premium)
        result = production*rate*(1 + premium/100)
    except ValueError:
        err_msg = 'Ощибка в значении!'
    except TypeError:
        err_msg = 'Ощибка Типа данных!'
    else:
        pass
    finally:
        pass
result_msg = err_msg if err_msg else f'Результат вычисления заработной платы: {result:.2f}'
print(result_msg)



