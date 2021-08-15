from storage_project_sp_obj import Catalog


class Storage(Catalog):

    _CATALOG_NAME = __qualname__
    _CATALOG_FILE_NAME = __qualname__ + '.json'
    _CATALOG_KEYS = ['address']
    _CATALOG_DICT = {}


if __name__ == '__main__':
    print('Модуль не предназначен для самостоятельной работы')
