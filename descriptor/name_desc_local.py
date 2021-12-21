

class Person:
    def __init__(self, name):
        self._name = name

    class Name:
        def __get__(self, instance, owner):
            print('fetch...')
            return instance._name

        def __set__(self, instance, value):
            print('change...')
            instance._name = value

        def __delete__(self, instance):
            print('remove...')
            del instance._name

    name = Name()
