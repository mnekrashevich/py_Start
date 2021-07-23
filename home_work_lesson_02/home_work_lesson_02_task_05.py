# coding=utf8

# 5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].

rating = []
print(rating)
while True:
    try:
        new_el = int(input('Введите натуральное число, для завершения введите 0: '))
        if new_el == 0:
            break
        elif new_el < 0:
            raise ValueError()
    except ValueError:
            print('Введено Неверное значение. Попробуйте еще раз.')
    else:
        #Ну самый короткий способ видимо так:
        rating.append(new_el)
        rating.sort(reverse=True)

        #Но если заморочится к понятию более близкому к рейтингу (это было бы актуальнее для структуры на словаре.
        #например {'john': 5, 'ivan':3, 'lena':3 .... } тогда для рейтинга имел бы значение порядок включения элементов
        #в словарь (cортировка не дает гарантию сохранения порядка)... тогда:
        # if  len(rating) == 0 or new_el <= rating[-1]: # Порядок условий важен, если поменять - на пустом списке - ошибка
        #     rating.append(new_el) #если вводимы элемент <= последнему или список пустой сразу лепим в конец списка.
        # else:
        #     for i in rating:
        #         if new_el > i: #Т.к. все числа натуральные и список ранее отсортирован, находим нужную позицию.
        #             rating.insert(rating.index(i),new_el)
        #             break

        print(rating)