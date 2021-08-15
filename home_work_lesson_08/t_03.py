class NotNumber(Exception):
    def __init__(self, err_obj):
        self.err_msg = f'Добавляемое(ые) значения содержат не числа <{err_obj}>. ' \
                       f'И добавлять мы их(его) не будем))). А остальное добавим. ' \
                       f'Если там что-то осталось)'

    def __str__(self):
        return self.err_msg


class NumList(list):

    @staticmethod
    def is_number(obj):
        return type(obj) in [int, float]

    def __init__(self, seq=()):
        try:
            not_num = [obj for obj in seq if not self.is_number(obj)]
            if not_num:
                raise NotNumber(not_num)
        except NotNumber as nn:
            print(nn)
        finally:
            is_num = [obj for obj in seq if self.is_number(obj)]
            super().__init__(is_num)

    def __str__(self):
        return repr(self)

    def append(self, __object) -> None:
        try:
            if not self.is_number(__object):
                raise NotNumber(__object)
        except NotNumber as nn:
            print(nn)
        else:
            super().append(__object)

    def extend(self, __iterable) -> None:
        try:
            not_num = [obj for obj in __iterable if not self.is_number(obj)]
            if not_num:
                raise NotNumber(not_num)
        except NotNumber as nn:
            print(nn)
        finally:
            is_num = [obj for obj in __iterable if self.is_number(obj)]
            super().extend(is_num)

    def insert(self, __index, __object) -> None:
        try:
            if not self.is_number(__object):
                raise NotNumber(__object)
        except NotNumber as nn:
            print(nn)
        else:
            super().insert(__index, __object)


nnn = NumList([1, 2.5, 6, -7])
print(nnn)
nnn = NumList(['1', 2.5, 6, -7])
print(nnn)
nnn.append('Ь')
print(nnn)
nnn.append(5)
print(nnn)
nnn.extend([1, 2, 41])
print(nnn)
nnn.extend(['sdf', 4])
print(nnn)
nnn.insert(3, 81)
print(nnn)
nnn.insert(2, 'Не прокатило')
print(nnn)
