import json
import uuid
import os


class Doc:

    _DOCS_NAME = __qualname__
    _DOCS_FILE_NAME = __qualname__ + '.json'
    _DOCS_DICT = {}

    def __init__(self, **kwargs):
        self.uid = kwargs.get('uid', '')
        self.number = kwargs.get('number', '')
        self.date = kwargs.get('date', '')
        self.storage = kwargs.get('storage', '')
        self.is_posting = kwargs.get('is_posting', False)
        self._DOCS_DICT[self.uid] = self
        self.rows = {}

    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, uid):
        if uid:
            self._uid = str(uid)
        else:
            self._uid = str(uuid.uuid4())

    def __str__(self):
        return f'#:{self.number}  {chr(8987)}:{self.date}'

    @classmethod
    def print_docs(cls):
        result = {}
        if not len(cls._DOCS_DICT):
            print('*'*50)
        for num, obj in enumerate(cls._DOCS_DICT.values(), 1):
            print(f'{num}: {obj}')
            result[num] = obj.uid
        return result

    def serialize_obj(self):
        result = self.__dict__.copy()
        result['uid'] = result.pop('_uid')
        return result

    @classmethod
    def serialize(cls):
        return [obj.serialize_obj() for obj in cls._DOCS_DICT.values()]

    @classmethod
    def dump_to_file(cls):
        with open(cls._DOCS_FILE_NAME, 'w', encoding='utf-8') as f_obj:
            json.dump(cls.serialize(), f_obj, ensure_ascii=False)

    @classmethod
    def load_from_file(cls):
        if os.path.exists(cls._DOCS_FILE_NAME):
            with open(cls._DOCS_FILE_NAME, 'r', encoding='utf-8') as f_obj:
                json_list = json.load(f_obj)
                for obj in json_list:
                    cls(**obj)

    @classmethod
    def interactive_choice(cls, __prompt):
        choice = None
        cat = cls.print_docs()
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


class ReceiptInvoice(Doc):

    _DOCS_NAME = __qualname__
    _DOCS_FILE_NAME = __qualname__ + '.json'
    _DOCS_DICT = {}


class ExpenseInvoice(Doc):

    _DOCS_NAME = __qualname__
    _DOCS_FILE_NAME = __qualname__ + '.json'
    _DOCS_DICT = {}


class InternalInvoice(Doc):

    _DOCS_NAME = __qualname__
    _DOCS_FILE_NAME = __qualname__ + '.json'
    _DOCS_DICT = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.to_storage = kwargs.get('to_storage', '')


class DocRow:
    pass


if __name__ == '__main__':
    print('Модуль не предназначен для самостоятельной работы')
