

class InstState:
    def __get__(self, instance, owner):
        print('InstState get')
        return instance._x * 10

    def __set__(self, instance, value):
        print('InstState set')
        instance._x = value


class CalcAttrs:
    x = InstState()
    y = 3

    def __init__(self):
        self._x = 2
        self.z = 4


if __name__ == '__main__':
    obj = CalcAttrs()
    print(obj.x, obj.y, obj.z)
    obj.x = 5
    CalcAttrs.y = 6
    obj.z = 7
    print(obj.x, obj.y, obj.z)

    obj2 = CalcAttrs()
    print(obj2.x, obj2.y, obj2.z)