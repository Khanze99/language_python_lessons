

class Attrs:
    def __getattr__(self, item):
        print(item)

    def __setattr__(self, key, value):
        print(key, value)


if __name__ == '__main__':
    a = Attrs()
    a.hello = 'world'
    print(a.hello)

    print(a.world)
    print(a['1'])