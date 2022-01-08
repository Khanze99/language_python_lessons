import sys


traceMe = True


class BuiltinMixin:
    def reroute(self, attr, *args, **kwargs):
        return self.__class__.__getattr__(self, attr)(*args, **kwargs)

    def __add__(self, other):
        return self.reroute('__add__', other)

    def __str__(self):
        return self.reroute('__str__')


def trace(*args):
    if traceMe: print('[' + ' '.join(map(str, args)) + ']')


def accessControl(failIf):
    def onDecorator(aClass):
        if __debug__:
            return aClass

        else:
            class onInstance(BuiltinMixin):
                def __init__(self, *args, **kwargs):
                    self.__wrapped = aClass(*args, **kwargs)

                def __getattr__(self, item):
                    trace('get: ', item)
                    if failIf(item):
                        raise TypeError('private attribute fetch: ' + item)

                    else:
                        return getattr(self.__wrapped, item)

                def __setattr__(self, key, value):
                    trace('set: ', key, value)

                    if key == '_onInstance__wrapped':
                        self.__dict__[key] = value
                    elif failIf(key):
                        raise TypeError('private attribute change: ' + key)
                    else:
                        setattr(self.__wrapped, key, value)
        return onInstance
    return onDecorator


def Private(*args):
    return accessControl(failIf=(lambda arg: arg in args))


def Public(*args):
    return accessControl(failIf=(lambda arg: arg not in args))


@Private('name')
class Person:
    def __init__(self, age, name, job):
        self.age = age
        self.name = name
        self.job = job

    @property
    def getFirstName(self):
        return self.name.split(' ')[0]

    def __add__(self, other):
        self.age += other

    def __str__(self):
        return f'{self.name} - {self.age}'


bob = Person(20, 'Bob Smith', 'dev')
print(bob.age)
bob + 20
print(bob)
print(bob.age)
print(bob.getFirstName)
print(bob.age)

bob.job = 'manager'
print(bob.job)


try: print(bob.name)
except TypeError: print(sys.exc_info())
