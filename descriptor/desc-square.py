

class DescSquare:
    def __init__(self, start):
        self.value = start

    def __get__(self, instance, owner):
        return self.value ** 2

    def __set__(self, instance, value):
        self.value = value


class Client1:
    x = DescSquare(5)


class Client2:
    x = DescSquare(20)


if __name__ == '__main__':
    c1 = Client1()
    c2 = Client2()

    print(c1.x)
    c1.x = 6

    print(c1.x)
    print(c2.x)
