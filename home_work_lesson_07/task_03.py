class Cell:

    def __init__(self, num):
        if num <= 0:
            raise ValueError('Должно быть больше 0')
        self.num = num

    def __add__(self, other):
        if type(other) != Cell:
            raise TypeError(f'Ошибка типа {other}. Ожидалось {Cell} не {type(other)}.')
        num = self.num + other.num
        return Cell(num)

    def __sub__(self, other):
        if type(other) != Cell:
            raise TypeError(f'Ошибка типа {other}. Ожидалось {Cell} не {type(other)}.')
        num = self.num - other.num
        if num <= 0:
            raise ValueError('Результат меньше 0. Невозможно выполнить операцию.')
        return Cell(num)

    def __mul__(self, other):
        if type(other) != Cell:
            raise TypeError(f'Ошибка типа {other}. Ожидалось {Cell} не {type(other)}.')
        num = self.num * other.num
        return Cell(num)

    def __truediv__(self, other):
        if type(other) != Cell:
            raise TypeError(f'Ошибка типа {other}. Ожидалось {Cell} не {type(other)}.')
        num = self.num // other.num
        if num <= 0:
            raise ValueError('Результат меньше 0. Невозможно выполнить операцию.')
        return Cell(num)

    def make_order(self, row_len):
        filled_rows = self.num//row_len
        tail_row = self.num % row_len
        return (('*' * row_len + '\n')*filled_rows + '*' * tail_row).strip()

    def __str__(self):
        row_len = round(self.num ** 0.5 + 0.5)
        return self.make_order(row_len)


ROW_LEN = 3

s1 = Cell(4)
print('s1')
print(s1.make_order(ROW_LEN))
print('-'*100)

s2 = Cell(2)
print('s2')
print(s2.make_order(ROW_LEN))
print('-'*100)

s1s2_add = s1 + s2
print('s1s2_add')
print(s1s2_add.make_order(ROW_LEN))
print('-'*100)

print('s1s2_sub')
try:
    s1s2_sub = s1 - s2
    print(s1s2_sub.make_order(ROW_LEN))
except (TypeError, ValueError) as ex:
    print(ex)
print('-'*100)

print('s2s1_sub')
try:
    s2s1_sub = s2 - s1
    print(s2s1_sub.make_order(ROW_LEN))
except (TypeError, ValueError) as ex:
    print(ex)
print('-'*100)

print('s1s2_truediv')
try:
    s1s2_truediv = s1 / s2
    print(s1s2_truediv.make_order(ROW_LEN))
except (TypeError, ValueError) as ex:
    print(ex)
print('-'*100)

print('s1s2_mul')
try:
    s1s2_mul = s1 * s2
    print(s1s2_mul.make_order(ROW_LEN))
except (TypeError, ValueError) as ex:
    print(ex)
print('-'*100)
