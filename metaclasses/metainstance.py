

class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
        print('MetaOne.new', classname)
        return type.__new__(meta, classname, supers, classdict)

    def toast(self):
        return 'toast'


class Super(metaclass=MetaOne):
    def spam(self):
        return 'spam'


class Sub(Super):
    def eggs(self):
        return 'eggs'
