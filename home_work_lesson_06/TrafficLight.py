# 1. Создать класс TrafficLight (светофор).
#
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный)
# — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение
# и завершать скрипт.
from datetime import datetime
from threading import Timer
from itertools import cycle


class TrafficLight:

    __delay_dict = {'red': 7, 'green': 10, 'yellow': 2}
    __colors = {'red': 'Красный', 'yellow': 'Желтый', 'green': 'Зеленый'}

    def __init__(self, street):
        self.__gen_colors = None
        self.__color = None
        self.__delay = 0
        self.__isEnable = False
        self.street = street

    def __turn_on(self):
        self.__isEnable = True
        self.__gen_colors = cycle(['red', 'yellow', 'green', 'yellow'])
        print(f'Светофор на улице {self.street} включен. {datetime.now().strftime("%Y-%m-%d-%H.%M.%S")}')
        self.__shedule_running()

    def __turn_off(self):
        self.__isEnable = False
        self.__gen_colors = None
        print(f'Светофор на улице {self.street} отключен. {datetime.now().strftime("%Y-%m-%d-%H.%M.%S")}')

    def __turn_color(self):
        self.__color = next(self.__gen_colors)
        self.__delay = self.__delay_dict[self.__color]
        print(f'Светофор на улице {self.street} переключился на {TrafficLight.__colors[self.__color]}.'
              f' {datetime.now().strftime("%Y-%m-%d-%H.%M.%S")}')

    def running(self, period):
        self.__turn_on()
        period_timer = Timer(period, self.__turn_off)
        period_timer.start()

    def __shedule_running(self):
        if self.__isEnable:
            self.__turn_color()
            color_timer = Timer(self.__delay, self.__shedule_running)
            color_timer.start()


if __name__ == '__main__':
    traffic_light_l = TrafficLight('ул. Ленина')
    traffic_light_l.running(100)
