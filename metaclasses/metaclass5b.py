

class SuperMeta(type):

    def __call__(meta, classname, supers, classdict):
        print('In SuperMeta.call:', classname)
        return type.__call__(meta, classname, supers, classdict)


class SubMeta(SuperMeta):
    def __init__(Class, classname, supers, classdict):
        print('In SubMeta.init: ', classname)


print(SubMeta.__class__)
print([n.__name__ for n in SubMeta.__mro__])
print(SubMeta.__call__)

SubMeta.__call__(SubMeta, 'xxx', (), {})
SubMeta('yyy', (), {})
