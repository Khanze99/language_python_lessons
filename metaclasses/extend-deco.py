

def eggsfunc(obj):
    return obj.value * 4


def hamfunc(obj, value):
    return value + 'ham'


def Extender(aClass):
    aClass.eggs = eggsfunc
    aClass.ham = hamfunc
    return aClass


@Extender
class Client1:
    def __init__(self, value):
        self.value = value

    def spam(self):
        return self.value * 2


@Extender
class Client2:
    value = 'ni?'


x = Client1('NI!')
print(x.spam())
print(x.eggs())
print(x.ham('bacon'))

y = Client2()
print(y.eggs())
print(y.ham('bacon'))