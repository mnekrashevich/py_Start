from abc import ABC, abstractmethod
from weakref import ref


class Clothes(ABC):

    MAX_SIZE = 0
    MIN_SIZE = 0
    __clothes_list = []

    @staticmethod
    def general_calculate():
        return round(sum([r().calculate() for r in Clothes.__clothes_list]), 3)

    def __init__(self, size):
        self.size = size
        self.__clothes_list.append(ref(self))

    def __del__(self):
        if ref(self) in self.__clothes_list:
            self.__clothes_list.remove(ref(self))

    @abstractmethod
    def calculate(self):
        return 0

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size > self.MAX_SIZE:
            self.__size = self.MAX_SIZE
        elif size < self.MIN_SIZE:
            self.__size = self.MIN_SIZE
        else:
            self.__size = size


class Suit(Clothes):

    MAX_SIZE = 14
    MIN_SIZE = 8

    def calculate(self):
        return round((2 * self.size + 0.3), 3)


class Coat(Clothes):

    MAX_SIZE = 25
    MIN_SIZE = 11

    def calculate(self):
        return round((self.size/6.5 + 0.5), 3)


s = Suit(3)
print('s', s.size, s.calculate())
print(Clothes.general_calculate())

c = Coat(80)
print('c', c.size, c.calculate())
print(Clothes.general_calculate())

s1 = Suit(15)
print('s1', s1.size, s1.calculate())
print(Clothes.general_calculate())

s1 = Suit(20)
print('s1', s1.size, s1.calculate())
print(Clothes.general_calculate())

del s1
print(Clothes.general_calculate())
print(s.general_calculate())
