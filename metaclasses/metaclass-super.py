

class SuperMetaObj:
    def __call__(self, classname, supers, classdict):
        print('In SuperMetaObj.call: ', classname, supers, classdict, sep='\n...')
        Class = self.__New__(classname, supers, classdict)
        self.__Init__(Class, classname, supers, classdict)
        return Class


class SubMetaObj(SuperMetaObj):
    def __New__(self, classname, supers, classdict):
        print('In SubMetaObj: ', classname, supers, classdict)
        return type(classname, supers, classdict)

    def __Init__(self, Class, classname, supers, classdict):
        print('In SubMetaObj: ', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))


class Eggs: pass


class Spam(Eggs, metaclass=SubMetaObj()):
    data = 1

    def meth(self, arg):
        return self.data + arg


x = Spam()
print(x)
print(x.data, x.meth(2))
