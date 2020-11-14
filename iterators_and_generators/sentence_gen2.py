import re
import reprlib


RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text

    def __iter__(self):
        for match in RE_WORD.finditer(self.text):  # finditer строит итератор, который обходит все соответствия текста
            # self.text регулярному выражению, порождая объекты MatchObject
            yield match.group()  # извлекает сопоставленный текст из объекта MatchObject

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)
