from collections import abc
from functools import singledispatch
import numbers
import html


@singledispatch  # @singledispatch помечает базовую функцию, которая обрабатывает тип object
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)


@htmlize.register(str)  # Каждая специализированная функция снабжается декоратором @base_function.register("type")
def _(text):  # Имена специализированных функций несущественны, и это подчеркнуто выбором _ в качестве имени
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)


@htmlize.register(numbers.Integral)  # Для каждого типа, нуждающегося в специальной обработке, регистрируется новая
# функция. numbers.Integral - виртуальный суперкласс int.
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)


@htmlize.register(tuple)  # Можно указывать несколько декораторов register, если требуется, чтобы
# одна функция поддерживала несколько типов.
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'


# PEP 443 – Single-dispatch generic functions» (https://www.python.org/dev/peps/
# pep-0443/