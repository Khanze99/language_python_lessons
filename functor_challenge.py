# Написать функтор для определения порядка сортировки списка p, состоящий из объектов класса Person
# То есть вызывая функтор с названием functor_name("surname") сортировка выполнялась бы по этому свойтсву. Если
# указать два значения, то сортировка делалась бы по фамилии, но при их равентсве - по имени

class Person:

    def __init__(self, surname, forename, old):
        self.surname = surname
        self.forename = forename
        self.old = old


p = [Person("Иванов", "Иван", 20),
     Person("Петров", "Степан", 21),
     Person("Сидоров", "Альберт", 25),
     Person("Кувыкин", "Иван", 21),
     Person("Абдуллин", "Иван", 28)]


def sort_key(persons: list):

    def sorted_from_key(*args):
        sorted_persons = persons
        if 'surname' in args:
            sorted_persons = sorted(persons, key=lambda person: person.surname)

        if 'forename' in args:
            sorted_persons = sorted(persons, key=lambda person: person.forename)

        if 'forename' in args and 'surname' in args:
            sorted_persons = sorted(persons, key=lambda person: person.forename and person.surname)

        return sorted_persons

    return sorted_from_key


sk = sort_key(p)
sk("surname", "forename")
