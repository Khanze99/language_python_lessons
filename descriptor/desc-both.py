

class DescBoth:
    def __init__(self, data):
        self.data = data

    def __get__(self, instance, owner):
        return f'{self.data}, {instance.data}'

    def __set__(self, instance, value):
        instance.data = value


class Client:
    def __init__(self, data):
        self.data = data

    managed = DescBoth('spam')


if __name__ == '__main__':
    i = Client('eggs')
    print(i.managed)
    i.managed = 'SPAM'
    print(i.managed)

    print(i.__dict__)
    print([x for x in dir(i) if not x.startswith('__')])
    print(getattr(i, 'data'))
    print(getattr(i, 'managed'))

    for attr in (x for x in dir(i) if not x.startswith('__')):
        print(f'{attr} => {getattr(i, attr)}')

