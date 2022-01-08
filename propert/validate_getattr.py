

class CardHolder:
    acctlen = 8
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    def __getattr__(self, item):
        if item == 'acct':
            return self._acct[:-3] + '***'
        elif item == 'remain':
            return self.retireage - self.age
        else:
            raise AttributeError(item)

    def __setattr__(self, key, value):
        if key == 'name':
            value = value.lower().replace(' ', '_')
        elif key == 'age':
            if value < 0 and value > 150:
                raise ValueError('invalid age')
        elif key == 'acct':
            key = '_acct'
            value = value.replace('-', '')
            if len(value) > self.acctlen:
                raise TypeError('invalid acct number')
        elif key == 'remain':
            raise TypeError('cannot set remain')
        self.__dict__[key] = value