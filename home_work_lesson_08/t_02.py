class MyZeroDivisionError(Exception):
    def __init__(self, *args, **kwargs):
        pass


class MyInt(int):
    def __init__(self, value: int):
        self.value = value

    def __truediv__(self, other):
        if other == 0:
            raise MyZeroDivisionError('Ай-йай: деление на ноль. Так нельзя делать!')
        else:
            return self.value/other


z = MyInt(4)
y = z/2
print('z =', z)
print('y = z / 2 =', y)
try:
    y = z / 0
except MyZeroDivisionError as MyEx:
    print(MyEx)



