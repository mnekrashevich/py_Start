# 3. Реализовать базовый класс Worker (работник).
#
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии
# (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name: str, surname: str, position: str, wage: float, bonus: float):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


if __name__ == '__main__':
    oleg = Position('Олег', 'Олегов', 'Директор', 100000, 50000)
    print(oleg.name)
    print(oleg.surname)
    print(oleg.position)
    print(oleg.get_full_name())
    print(oleg.get_total_income())

    ne_oleg = Position('Анна', 'Романова', 'Бухгалтер', 110000, 20000)
    print(ne_oleg.name)
    print(ne_oleg.surname)
    print(ne_oleg.position)
    print(ne_oleg.get_full_name())
    print(ne_oleg.get_total_income())
