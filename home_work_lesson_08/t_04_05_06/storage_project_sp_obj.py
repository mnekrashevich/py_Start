import json
import uuid
import os


class Catalog:
    _CATALOG_NAME = __qualname__
    _CATALOG_FILE_NAME = __qualname__ + '.json'
    _CATALOG_KEYS = []
    _CATALOG_DICT = {}

    def __init__(self, **kwargs):
        self.uid = kwargs.get('uid', '')
        self.name = kwargs.get('name', '')
        for key in self._CATALOG_KEYS:
            self.__dict__[key] = kwargs.get(key, '')
        self._CATALOG_DICT[self.uid] = self

    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, uid):
        if uid:
            self._uid = str(uid)
        else:
            self._uid = str(uuid.uuid4())

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name:
            self._name = str(name)
        else:
            self._name = '<--->'

    def __str__(self):
        attrs_values = '<'
        for key, value in self.__dict__.items():
            if key in self._CATALOG_KEYS:
                attrs_values += f'{key}: {value}; '
        attrs_values = attrs_values[:-2] + '>'
        return f'{self.name} {attrs_values}'

    @classmethod
    def print_catalog(cls):
        result = {}
        if not len(cls._CATALOG_DICT):
            print('*'*10 + 'Нет элементов для отображения' + '*'*10)
        for num, obj in enumerate(cls._CATALOG_DICT.values(), 1):
            print(f'{num}: {obj}')
            result[num] = obj.uid
        return result

    def serialize_obj(self):
        result = self.__dict__.copy()
        result['uid'] = result.pop('_uid')
        result['name'] = result.pop('_name')
        return result

    @classmethod
    def serialize(cls):
        return [obj.serialize_obj() for obj in cls._CATALOG_DICT.values()]

    @classmethod
    def dump_to_file(cls):
        with open(cls._CATALOG_FILE_NAME, 'w', encoding='utf-8') as f_obj:
            json.dump(cls.serialize(), f_obj, ensure_ascii=False)

    @classmethod
    def load_from_file(cls):
        if os.path.exists(cls._CATALOG_FILE_NAME):
            with open(cls._CATALOG_FILE_NAME, 'r', encoding='utf-8') as f_obj:
                json_list = json.load(f_obj)
                for obj in json_list:
                    cls(**obj)

    @classmethod
    def interactive_choice(cls, __prompt):
        choice = None
        cat = cls.print_catalog()
        if not len(cat):
            print('Нет вариантов для выбора.')
            return choice
        else:
            try:
                choice = cat[int(input(__prompt))]
            except (ValueError, IndexError):
                print('Неверный выбор')
            finally:
                return choice

    @classmethod
    def interactive_add(cls):
        kwargs = {'name': input('Name: ')}
        for key in cls._CATALOG_KEYS:
            kwargs[key] = input(f'{key.title()}: ')
        cls(**kwargs)

    @classmethod
    def interactive_delete(cls):
        uid_to_del = cls.interactive_choice('Выбрать вариант для удаления: ')
        if uid_to_del:
            cls._CATALOG_DICT.pop(uid_to_del)


if __name__ == '__main__':
    print('Модуль не предназначен для самостоятельной работы')
