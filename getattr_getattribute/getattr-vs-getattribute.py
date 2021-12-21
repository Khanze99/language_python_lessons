

class GetAttr:
    attr1 = 1

    def __init__(self):
        self.attr2 = 2

    def __getattr__(self, item):
        print(f'get: {item}')

        if item == 'attr3':
            return 3
        else:
            raise AttributeError(item)


x = GetAttr()
print(x.attr1)
print(x.attr2)
print(x.attr3)
print('=' * 20)


class GetAttribute:
    attr1 = 1

    def __init__(self):
        self.attr2 = 2

    def __getattribute__(self, item):
        print(f'get: {item}')

        if item == 'attr3':
            return 3
        else:
            return object.__getattribute__(self, item)


x = GetAttribute()
print(x.attr1)
print(x.attr2)
print(x.attr3)