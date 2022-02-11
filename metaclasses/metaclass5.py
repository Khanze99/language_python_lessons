

class SuperMeta(type):
    def __call__(meta, classname, supers, classdict):
        print('In SuperMeta.call: ', classname, supers, classdict, sep='\n...')
        return type.__call__(meta, classname, supers, classdict)

    def __init__(Class, classname, supers, classdict):
        print('In SuperMeta init:', classname, supers, classdict)
        print('... init class objects:', list(Class.__dict__.keys()))


print('making metaclass')


class SubMeta(type, metaclass=SuperMeta):
    def __new__(meta, classname, supers, classdict):
        print('In SubMeta.new:', classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)

    def __init__(Class, classname, supers, classdict):
        print('In SubMeta init:', classname, supers, classdict)
        print('... init class object:', list(Class.__dict__.keys()))


class Eggs: pass


print('making class')


class Spam(Eggs, metaclass=SubMeta):
    data = 1

    def meth(self, arg):
        return self.data + arg


x = Spam()
print(x.data, x.meth(3))