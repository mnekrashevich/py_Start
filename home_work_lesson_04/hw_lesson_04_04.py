# coding=utf8
# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел, соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

x = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
y = [z for z in x if x.count(z)==1]
print(f'исходный список {x}')
print(f'результирующий список {y}')

