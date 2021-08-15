class Date:

    @classmethod
    def str_to_date(cls, text_date):
        day, month, year = text_date.split('-')
        day, month, year = int(day), int(month), int(year)
        return day, month, year

    @staticmethod
    def check_date(day, month, year):
        if year <= 0:
            raise ValueError('Что-то с годом не то')
        if not 0 < month <= 12:
            raise ValueError('Что то с месяцем не то')
        max_feb_day = 29 if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else 28
        max_day_num = 31 if month in [1, 3, 5, 7, 8, 10, 12] else 30 if month != 2 else max_feb_day
        if not 0 < day <= max_day_num:
            raise ValueError('Что то с днем не то')

    def __init__(self, text_date):
        dmy = self.str_to_date(text_date)
        self.check_date(*dmy)
        self.day, self.month, self.year = dmy

    def __str__(self):
        return f'{self.day:02}-{self.month:02}-{self.year:04}'


x = Date('29-03-2001')
print(x)
