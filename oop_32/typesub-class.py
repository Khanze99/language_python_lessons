

class MyList(list):
    def __getitem__(self, item):
        print(f'(indexing {self} at {item})')
        return list.__getitem__(self, item - 1)


if __name__ == '__main__':
    print(list('abc'))
    x = MyList('abc')
    print(x)
    print(x[1])
    print(x[3])
    x.append('spam')
    print(x)
    x.reverse()
    print(x)