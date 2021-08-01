# coding=utf8

# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
#  название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
#  Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
#  Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
import re, json

filename = '007.txt'
mode = 'r'
result_name = '007_result.txt'
mode_w = 'w'
with open(filename, mode, encoding='utf-8') as file, open(result_name, mode_w, encoding='utf-8') as result:
    str_lines = file.readlines()
    total = 0
    total_n = 0
    my_dict = {}

    for i_str in str_lines:
        name, _, revenue, costs = re.split('\t+',i_str.strip())
        revenue, costs = float(revenue), float(costs)
        profit = revenue-costs
        total += profit if profit >= 0 else 0
        total_n += 1 if profit >= 0 else 0
        my_dict[name] = profit
    my_list = [my_dict, {'average_profit': round(total/total_n if total_n else 0, 2)}]
    json.dump(my_list, result)