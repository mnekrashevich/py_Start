from storage_project_Storage import Storage
from storage_project_Equipment import Printer, Scanner, Laptop
from storage_project_Doc import ReceiptInvoice, ExpenseInvoice, InternalInvoice
# from storage_project_Report import Goods


def exit_storage():
    Storage.dump_to_file()
    Printer.dump_to_file()
    Scanner.dump_to_file()
    Laptop.dump_to_file()


def enter_storage():
    Storage.load_from_file()
    Printer.load_from_file()
    Scanner.load_from_file()
    Laptop.load_from_file()


class Command:
    def __init__(self, num, name, func, args, menu):
        self.num = num
        self.name = name
        self.func = func
        self.args = args
        self.menu = menu

    def __str__(self):
        return f'{self.num}: {self.name}'

    def execute_command(self):
        self.func(*self.args)
        print('*'*50)
        if self.menu:
            self.menu.show()


class Menu:

    instance = None

    def __new__(cls):
        if not cls.instance:
            cls.instance = super(Menu, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.current_option = 1
        self.options = \
            {
                1: (
                    'Главное меню',
                    [
                        Command(1, 'Справочник Склады', self.change_option, [2], self),
                        Command(2, 'Справочник Принтеры', self.change_option, [3], self),
                        Command(3, 'Справочник Сканеры', self.change_option, [4], self),
                        Command(4, 'Справочник Ноутбуки', self.change_option, [5], self),
                        Command(5, 'Приход', self.change_option, [6], self),
                        Command(6, 'Расход', self.change_option, [7], self),
                        Command(7, 'Перемещение', self.change_option, [8], self),
                        Command(8, 'Отчет по остаткам', self.change_option, [9], self),
                        Command(9, 'Завершить работу', exit_storage, [], None)
                    ]
                    ),
                2: (
                    'Cклады',
                    [
                        Command(1, 'Добавить склад', Storage.interactive_add, [], self),
                        Command(2, 'Удалить склад', Storage.interactive_delete, [], self),
                        Command(3, 'Показать склады', Storage.print_catalog, [], self),
                        Command(4, 'Вернуться в главное меню', self.change_option, [1], self)
                    ]
                    ),
                3: (
                    'Принтеры',
                    [
                        Command(1, 'Добавить принтер', Printer.interactive_add, [], self),
                        Command(2, 'Удалить принтер', Printer.interactive_delete, [], self),
                        Command(3, 'Показать принтеры', Printer.print_catalog, [], self),
                        Command(4, 'Вернуться в главное меню', self.change_option, [1], self)
                    ]
                    ),
                4: (
                    'Сканеры',
                    [
                        Command(1, 'Добавить сканер', Scanner.interactive_add, [], self),
                        Command(2, 'Удалить сканер', Scanner.interactive_delete, [], self),
                        Command(3, 'Показать сканеры', Scanner.print_catalog, [], self),
                        Command(4, 'Вернуться в главное меню', self.change_option, [1], self)
                    ]
                    ),
                5: (
                    'Ноутбуки',
                    [
                        Command(1, 'Добавить ноутбук', Laptop.interactive_add, [], self),
                        Command(2, 'Удалить ноутбук', Laptop.interactive_delete, [], self),
                        Command(3, 'Показать ноутбуки', Laptop.print_catalog, [], self),
                        Command(4, 'Вернуться в главное меню', self.change_option, [1], self)
                    ]
                    ),
                6: (
                    'Приходные документы',
                    [
                        Command(1, 'Добавить приход', Laptop.interactive_add, [], self),
                        Command(2, 'Удалить приход', Laptop.interactive_delete, [], self),
                        Command(3, 'Показать документы', Laptop.print_catalog, [], self),
                        Command(4, 'Вернуться в главное меню', self.change_option, [1], self)
                    ]
                    ),
                7: (
                    'Расходные документы',
                    [
                        Command(1, 'Добавить расход', Laptop.interactive_add, [], self),
                        Command(2, 'Удалить расход', Laptop.interactive_delete, [], self),
                        Command(3, 'Показать документы', Laptop.print_catalog, [], self),
                        Command(4, 'Вернуться в главное меню', self.change_option, [1], self)
                    ]
                    ),
                8: (
                    'Документы по внутреннему перемещению',
                    [
                        Command(1, 'Добавить внутреннее перемещение', Laptop.interactive_add, [], self),
                        Command(2, 'Удалить внутреннее перемещение', Laptop.interactive_delete, [], self),
                        Command(3, 'Показать документы', Laptop.print_catalog, [], self),
                        Command(4, 'Вернуться в главное меню', self.change_option, [1], self)
                    ]
                    )
            }

    def change_option(self, option):
        self.current_option = option

    def show(self):
        current_option = self.options[self.current_option]
        print(f'**********---{current_option[0]}---**********')
        for option in current_option[1]:
            print(option)
        try:
            choice = current_option[1][int(input('Выбрать вариант: '))-1]
        except (ValueError, IndexError):
            print('Неверный выбор')
            print('*'*50)
            self.show()
        else:
            choice.execute_command()


if __name__ == '__main__':
    print('Модуль не предназначен для самостоятельной работы')
