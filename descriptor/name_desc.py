

class Name:
    "name descriptor docs"

    def __get__(self, instance, owner):
        print("fetch")
        return instance._name

    def __set__(self, instance, value):
        print("change...")
        instance._name = value

    def __delete__(self, instance):
        print("remove...")
        del instance._name


class Person:
    def __init__(self, name):
        self._name = name
    name = Name()


if __name__ == "__main__":
    bob = Person("Bob")
    print(bob.name)
    bob.name = "Sue"
    print(bob.name)
    del bob.name

    print("-"*20)
    sue = Person("Sue")
    print(sue.name)
    print(Name.__doc__)
