# 4. Реализуйте базовый класс Car.
#
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
# turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, default_speed, color, name):
        self.default_speed = default_speed
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def go(self, *args):
        self.speed = self.default_speed if len(args) == 0 else args[0]
        if self.speed <= 0:
            print(f'машина {self.name} сделала попытку поехать')
        else:
            print(f'машина {self.name} поехала')

    def stop(self):
        self.speed = 0
        print(f'машина {self.name} остановилась')

    def turn(self, direction):
        dict_direction = {'left': 'повернула налево', 'right': 'повернула направо', 'back': 'развернулась'}
        if dict_direction.get(direction):
            print(f'машина {self.name} {dict_direction[direction]}')
        else:
            print(f'машина {self.name} выполнила неизвестный маневр')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):

    def show_speed(self):
        print(self.speed)
        if self.speed > 60:
            print('Превышение скорости')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        print(self.speed)
        if self.speed > 40:
            print('Превышение скорости')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


if __name__ == '__main__':
    t_car = TownCar(60, 'Красный', 'lexus')
    t_car.go(0)
    t_car.show_speed()
    t_car.go()
    t_car.show_speed()
    t_car.go(70)
    t_car.show_speed()
    t_car.turn('left')
    t_car.stop()
    t_car.show_speed()

    w_car = WorkCar(40, 'yellow', 'jsv')
    w_car.go()
    w_car.turn('up')
    w_car.stop()
    print(w_car.color)
    w_car.show_speed()
    w_car.go()
    w_car.show_speed()
    w_car.go(90)
    w_car.show_speed()
    print(f'{w_car.name} {w_car.is_police} police')

    p_car = PoliceCar(120, 'white-blue', 'uaz')
    print(f'{p_car.name} {p_car.is_police} police')

    s_car = SportCar(200, 'red', 'lotus')
    s_car.go()
    s_car.show_speed()
    p_car.go(s_car.speed+10)
    p_car.show_speed()
    s_car.stop()
    p_car.stop()
