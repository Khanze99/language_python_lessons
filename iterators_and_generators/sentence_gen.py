import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:  # обходим self.words
            yield word  # отдаем текущее слово
        return   # Этот return не нужен; функция может просто "провалиться" и вернет управление автоматически. В любом
        # случае генераторная функция не возбуждает исключение StopIteration: когда значений не остается, она просто
        # выходит


s = Sentence('Hello my .., dear world!')
iter_s = iter(s)
print(next(iter_s))
print(next(iter_s))
print(next(iter_s))
print(next(iter_s))
