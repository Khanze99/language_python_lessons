

class Client1:
    def __init__(self, value):
        self.value = value

    def spam(self):
        return self.value * 2


class Client2:
    value = 'ni?'


def eggsfunc(obj):
    return obj.value * 4


def hamfunc(obj, value):
    return value + 'ham'


Client1.eggs = eggsfunc
Client1.ham = hamfunc

Client2.eggs = eggsfunc
Client2.ham = hamfunc


x = Client1('NI!')
print(x.spam())
print(x.eggs())
print(x.ham('bacon'))

y = Client2()
print(y.eggs())
print(y.ham('bacon'))