class ComplexNum():

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNum(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return ComplexNum(self.real * other.real - self.imag * other.imag, self.real*other.imag + other.real*self.imag)

    def __str__(self):
        prefix = '' if self.real == 0 else self.real
        postfix = f'+{self.imag}j' if self.imag > 0 else f'{self.imag}j' if self.imag < 0 else ''
        return f'{prefix}{postfix}'


x = complex(1, -8)
y = complex(8, -1)
print(x + y)
print(x * y)
print(x + 2)

print('-'*30)

xx = ComplexNum(1, -8)
yy = ComplexNum(8, -1)
print(xx + yy)
print(xx*yy)
print(xx + 2)

