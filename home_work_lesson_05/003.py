#coding=utf8

filename = 'emp_pay'
mode = 'r'
with open(filename, mode, encoding='utf-8') as file:
    str_lines = file.readlines()
    total = 0
    for i_str in str_lines:
        emp_name, pay = i_str.split()
        pay = int(pay)
        if pay < 20000:
            print(f'оплата сотрудника {emp_name} менее 20000 - {pay}')
        total += pay
    print(f'Средняя оплата {total/len(str_lines):.2f}')
