# Создайте менеджер контекста для безопасной обработки элементов словаря. В случае возникновения исключения словарь
# должен оставаться без изменений. Иначе(при успешной работе) он сохранял бы все изменения.
from contextlib import contextmanager
from copy import deepcopy


class DictManager:

    def __init__(self, d):
        self.__d = d

    def __enter__(self):
        self.__temp = self.__d.copy()
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__d.update(self.__temp)
        if exc_type:
            self.__temp = self.__d

        return True


d = {'name': 'Anvar', 'style': 'cool'}

with DictManager(d) as dm:
    dm['style'] = 'champion'
    print(dm['s'])

print(d)


d = {'name': 'Anvar', 'style': 'cool'}


@contextmanager
def save_dict(d):
    original_dict = d
    try:
        copy_dict = deepcopy(original_dict)
        yield copy_dict
        original_dict.clear()
        original_dict.update(copy_dict)
    except Exception:
        ...


with save_dict(d) as dm:
    dm['style'] = 'champion'
    print(dm['k'])

print(d)
