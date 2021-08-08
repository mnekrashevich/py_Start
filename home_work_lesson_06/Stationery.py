# 5. Реализовать класс Stationery (канцелярская принадлежность).
#
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:

    def __init__(self, title: str):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'я ручка {self.title}:)')


class Pencil(Stationery):
    def draw(self):
        print(f'я карандашик {self.title}:)')


class Handle(Stationery):
    def draw(self):
        print(f'iМаркер {self.title}:)')


if __name__ == '__main__':
    h = Handle('Даша')
    p = Pen('Виталик')
    pp = Pencil('Петя')
    h.draw()
    p.draw()
    pp.draw()
