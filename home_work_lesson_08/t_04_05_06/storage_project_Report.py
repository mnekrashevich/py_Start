class Report:
    def __init__(self, date):
        self.date = date


class Goods(Report):
    def __init__(self, date, storage):
        super().__init__(date)
        self.storage = storage


if __name__ == '__main__':
    print('Модуль не предназначен для самостоятельной работы')
