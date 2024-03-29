# coding=utf8

# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_info(**kwargs):
    """
    Функция принимает именованные параметры и выводит их строкой.
    В ключах знак "_" заменяется пробелом; Первая буква ключа в верхнем регистре остальные в нижнем
    ...
    Пример:
    user_info(name = 'name', surname = 'surname') --> Name - name; Surname - surname
    """
    result = '; '.join([f'{key.replace("_"," ").capitalize()} - {value}' for key, value in kwargs.items()])
    print('; '.join([f'{key.replace("_"," ").capitalize()} - {value}' for key, value in kwargs.items()]))
    return result


# Test:
# Передаем параметры справочником
kwargs = {'Имя':'Вася','Фамилия':'Иванов'}
user_info(**kwargs)
# Пердаем именованные параметры
user_info(имя = 'Васислий', фамилия = 'Васильев', отчество = 'Васильевич',
          год_рождения = '1984', город_проживания = 'Москва', email = 'vas_vas@mail.ru', телефон = '+7-999-000-00-00')
