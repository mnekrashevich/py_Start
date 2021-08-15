from storage_project_sp_obj import Catalog


class Equipment(Catalog):

    _CATALOG_NAME = __qualname__
    _CATALOG_FILE_NAME = __qualname__ + '.json'
    _CATALOG_KEYS = ['manufacturer', 'model_number']
    _CATALOG_DICT = {}
    _EQUIPMENT_TYPE = ''

    def __init__(self, **kwargs):
        self.equipment_type = self._EQUIPMENT_TYPE
        super().__init__(**kwargs)


class Printer(Equipment):

    _CATALOG_NAME = __qualname__
    _CATALOG_FILE_NAME = __qualname__ + '.json'
    _CATALOG_KEYS = ['manufacturer', 'model_number'] + ['is_color', 'paper_size']
    _CATALOG_DICT = {}
    _EQUIPMENT_TYPE = 'Printer'


class Scanner(Equipment):

    _CATALOG_NAME = __qualname__
    _CATALOG_FILE_NAME = __qualname__ + '.json'
    _CATALOG_KEYS = ['manufacturer', 'model_number'] + ['is_color', 'paper_size']
    _CATALOG_DICT = {}
    _EQUIPMENT_TYPE = 'Scanner'


class Laptop(Equipment):

    _CATALOG_NAME = __qualname__
    _CATALOG_FILE_NAME = __qualname__ + '.json'
    _CATALOG_KEYS = ['manufacturer', 'model_number'] + ['display_size', 'cpu', 'memory', 'os']
    _CATALOG_DICT = {}
    _EQUIPMENT_TYPE = 'Laptop'


if __name__ == '__main__':
    Printer.interactive_add()
    Printer.dump_to_file()
    Scanner.interactive_add()
    Scanner.dump_to_file()
    Laptop.interactive_add()
    Laptop.dump_to_file()
    print('Модуль не предназначен для самостоятельной работы')
