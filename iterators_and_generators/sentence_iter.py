import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):  # единетсвенное дополнение к предыдущей реализации Sentence.
        return SentenceIterator(self.words)  # выполняет требования протокола итерируемого объекта - создает и
        # возвращает итератор


class SentenceIterator:

    def __init__(self, words):
        self.words = words  # хранит ссылку на список слов
        self.index = 0  # использует для определения следующего слова

    def __next__(self):
        try:
            word = self.words[self.index]  # Получаем слово с индексом self.index
        except IndexError:
            raise StopIteration()  # вызываем исключения StopIteration, если закончились объекты и было
            # исключение IndexError

        self.index += 1  # Контроллируем индексы, увеличивая их на 1
        return word  # возвращаем слово по индексу

    def __iter__(self):  # реализация метода self.__iter__
        return self
