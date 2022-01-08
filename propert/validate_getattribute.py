
class CardHolder:
    acctlen = 8
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    def __getattribute__(self, item):
        superget = object.__getattribute__
        if item == 'acct':
            return superget(self, 'acct')[:-3] + '***'
        elif item == 'remain':
            return superget(self, 'retireage') - superget(self, 'age')
        else:
            return superget(self, item)

    def __setattr__(self, key, value):
        if key == 'name':
            value = value.lower().replace(' ', '_')
        elif key == 'age':
            if value < 0 and value > 150:
                raise ValueError('invalid age')
        elif key == 'acct':
            value = value.replace('-', '')
            if len(value) > self.acctlen:
                raise TypeError('invalid acct number')
        elif key == 'remain':
            raise TypeError('cannot set remain')
        self.__dict__[key] = value