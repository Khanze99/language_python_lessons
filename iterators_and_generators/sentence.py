import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text: str):
        self.text = text
        self.words = RE_WORD.findall(text)  # возвращает список всех непересекающихся подстрок, соответсвующих
        # регулярному выражению

    def __getitem__(self, index):
        return self.words[index]  # содержит результат .findall, поэтому мы просто возвращаем слово с заданным индексом

    def __len__(self):  # Чтобы выполнить требования протокола последовательности, мы реализуем метод __len__, - но для
        # получения итерируемого объекто он не нужен
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)  # Служебная функция reprlib.repr генерирует сокращенные
        # строковые представления структур данных, которые могут быть очень велики


s = Sentence('»The time has come,» the Walrus said,')  # по строке создается предложение - объекта класса Sentence
print(s)  # Обратите внимание на результат __repr__ - строку, содержащую многоточие, которая была
# сгенерирована функцией reprlib.repr

for word in s:  # Объекты Sentence являются итерируемыми, скоро мы в этом убедимся
    print(word)  # попробуйте закомментировать метод __getitem__ и вы убедитесь что будет исключение

print(list(s))  # Будучи итерируемыми, объекты могут быть использованы для конструирования списков и других
# итерируемых типов

print(s[0])
