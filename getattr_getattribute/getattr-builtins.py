

class GetAttr:
    eggs = 88

    def __init__(self):
        self.spam = 77

    def __len__(self):
        print('__len__: 42')
        return 42

    def __getattr__(self, item):
        print(f'getattr: {item}')
        if item == '__str__':
            return lambda *args: '[Getattr str]'
        else:
            return lambda *args: None


class GetAttribute:
    eggs = 88

    def __init__(self):
        self.spam = 77

    def __len__(self):
        print('__len__: 42')
        return 42

    def __getattribute__(self, item):
        print(f'gettatribute: {item}')
        if item == '__str__':
            return lambda *args: '[GettAttribute str]'
        else:
            return lambda *args: None


for Class in GetAttr, GetAttribute:
    print('\n' + Class.__name__.ljust(50, '='))
    x = Class()
    print(x.eggs)
    print(x.spam)
    print(x.other)
    len(x)

    try: x[0]
    except: print('fail []')

    try: x + 99
    except: print('fail +')

    try: x()
    except: print('fail ()')

    x.__call__()
    print(x.__str__())
    print(x)