

class Person:
    def __init__(self, name):
        self._name = name

    def __getattribute__(self, item):
        print(f'get: ' + item)
        if item == 'name':
            item = '_name'
        return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        print(f'set: {key} {value}')
        if key == 'name':
            key = '_name'
        self.__dict__[key] = value

    def __delattr__(self, item):
        print(f'delete: {item}')
        if item == 'name':
            item = '_name'

        del self.__dict__[item]


if __name__ == '__main__':
    bob = Person('Bob')
    print(bob.name)
    bob.name = 'Robert'
    print(bob.name)
    del bob.name
    print('-'*20)
    sue = Person('Sue')
    print(sue.name)