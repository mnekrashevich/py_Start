class Matrix:

    @staticmethod
    def is_in_types(*args):
        target, *target_types = args
        return type(target) in target_types

    def __new__(cls, list_of_list):
        # Проверям при созданнии входящие параметры.
        # Для теста представим что нам нужно не упасть с ошибкой при коячных параметрах а вернуть объект
        # другого класса, строку с описанием ошибки - хоть как то оправдаем для себя возможность перегрузки __new__:)
        try:
            if not cls.is_in_types(list_of_list, list):
                raise TypeError('Не список')  # На входе список?
            if False in [cls.is_in_types(i, list) for i in list_of_list]:
                raise TypeError('Не список списков')  # Это список списков?
            for i in list_of_list:
                for j in i:
                    if not cls.is_in_types(j, int, float):
                        raise TypeError('Не числа в списке списков')  # Все элементы списка списков числа?
            if len(set([len(i) for i in list_of_list])) != 1:
                raise ValueError('Строки списка разной длины')  # все списки одной длины
        except (TypeError, ValueError) as my_ex:
            return str(my_ex)
        else:
            instance = super().__new__(cls)
            return instance

    def __init__(self, list_of_list):
        self.__elements = list_of_list
        self.__rows = len(list_of_list)
        self.__cols = len(list_of_list[0])

    def __str__(self):
        field_len = self.__max_len_str_el() + 1
        return '\n'.join(''.join(f'{j:>{field_len}}' for j in i) for i in self.__elements)

    def __max_len_str_el(self):
        return max([max(map(lambda x: len(str(x)), i)) for i in self.__elements])

    def __add__(self, other):
        # Можно было бы через try вернуть в резултат строку с ошибкой, но пусть будет так
        if not Matrix.is_in_types(other, Matrix):
            raise TypeError(f'Тип второго операнда {type(other)}. Ожидалось {Matrix} ')
        if self.__cols != other.__cols or\
                self.__rows != other.__rows:
            raise ValueError('Размерности матриц отличаются')
        new_instance = Matrix([list(map(sum, zip(i, j))) for i, j in zip(self.__elements, other.__elements)])
        return new_instance


print("Matrix('asdf'):\n", Matrix('asdf'))
print("Matrix(['qw3r', 45]):\n", Matrix(['qw3r', 45]))
print("Matrix([[1, 2], [3, '3']]):\n", Matrix([[1, 2], [3, '3']]))
print("Matrix([[1, 2], [3, 4], [5, 6, 7]]):\n", Matrix([[1, 2], [3, 4], [5, 6, 7]]))
print("Matrix([[1, 2], [3, 4], [5, 6]]):")
print(Matrix([[1, 2], [3, 4], [5, 6]]))
print('-'*30)

foo = Matrix([[1, 2], [3, 4]])
print('foo:', type(foo), ':')
print(foo)

spam = Matrix([[4, 3], [2, 1]])
print('spam:', type(spam), ':')
print(spam)

bar = Matrix([[-1, -2], [-3, -4], [2, 3]])
print('bar:', type(bar), ':')
print(bar)
print('-'*30)

try:
    print('foo + bar')
    print(foo + bar)
except (TypeError, ValueError) as ex:
    print('Ошибка: ', ex)
print('-'*30)
try:
    print('foo + "Строка"')
    print(foo + 'Строка')
except (TypeError, ValueError) as ex:
    print('Ошибка: ', ex)
print('-'*30)
try:
    print('"Строка" + foo')
    print('Строка' + foo)
except (TypeError, ValueError) as ex:
    print('Ошибка: ', ex)
print('-'*30)
try:
    print('foo + spam')
    print(foo + spam)
except (TypeError, ValueError) as ex:
    print('Ошибка: ', ex)
print('-'*30)
