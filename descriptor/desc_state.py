

class DescState:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        print('DescState get')
        return self.value * 10

    def __set__(self, instance, value):
        print('DescState set')
        self.value = value


# Клиентский класс
class CalcAttrs:
    x = DescState(2)
    y = 3

    def __init__(self):
        self.z = 4


obj = CalcAttrs()
print(obj.x, obj.y, obj.z)
obj.x = 5
CalcAttrs.y = 6
obj.z = 7

print(obj.x, obj.y, obj.z)

obj2 = CalcAttrs()
print(obj2.x, obj2.y, obj2.z)
