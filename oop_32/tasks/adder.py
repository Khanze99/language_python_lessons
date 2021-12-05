"""
Наследование.
    Напишите класс по имени Adder, который экспортирует метод
    add (self, х, у), выводящий сообщение Not Implemented (Не реализован).

    Затем определите два подкласса класса Adder, которые реализуют метод add:
        ListAdder
    С методом add, который возвращает сцепление своим двух списковых аргу­
    ментов.
        DictAdder
    С методом add, который возвращает новый словарь, содержащий элементы
    из его двух словарных аргументов (подойдет любое определение словарного
    дополнения).

Поэкспериментируйте с интерактивным созданием экземпляров всех трех клас­
сов и вызовом их методов add. Затем расширьте суперкласс Adder для сохра­
нения объекта в экземпляре с помощью конструктора (например, присвоив
self .data список или словарь) и перегрузите операцию + посредством мето­
да __ add__ , чтобы автоматически направлять его вашим методам add (скажем,
X + Y запускает X. add (X.data, Y)). Где лучше всего разместить конструкторы и
методы перегрузки операций (т.е. в каких классах)? Какие разновидности объек­
тов вы можете добавлять в экземпляры своих классов?

На практике вы можете обнаружить, что методы add легче реализовать для при­
ема только одного реального аргумента (например, add (self, у)) и добавлять
этот один аргумент к текущим данным экземпляра (наподобие self .data + у).
Имеет ли больше смысла поступать так, чем передавать add два аргумента?
Сказали бы вы, что в итоге классы стали более “объектно-ориентированными”?


"""

from abc import ABC, abstractmethod
from typing import List, Dict, Union


class Adder(ABC):
    def __init__(self, data: Union[List, Dict]):
        self.data = data

    @abstractmethod
    def add(self, other):
        pass

    def __add__(self, other):
        return self.add(other)


class ListAdder(Adder):
    def add(self, other: List):
        return self.data + other


class DictAdder(Adder):
    def add(self, other: Dict):
        data = {**self.data, **other}
        return data


if __name__ == '__main__':
    test_list = [33, 99, 111]
    l = ListAdder([1, 2, 3])
    print(l.add(test_list))
    print(l + test_list)

    test_dict = {'A': 1, 'K': 99}
    d = DictAdder(dict(href='href', gg='pzdc'))
    print(d.add(test_dict))
    print(d + test_dict)