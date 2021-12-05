

class ListTree:
    def __attrnames(self, obj, indent):
        spaces = ' ' * (indent + 1)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += spaces + f'{attr}\n'
            else:
                result += spaces + f'{attr}={getattr(self, attr)}\n'
        return result

    def __listclass(self, aClass, indent):
        dots = '.' * indent
        if aClass in self.__visited:
            return f'\n{dots}<Class {aClass.__name__}, address {id(self)}: (see above)>\n'
        else:
            self.__visited[aClass] = True
            here = self.__attrnames(aClass, indent)
            above = ''

            for super_ in aClass.__bases__:
                above += self.__listclass(super_, indent+4)

            return f'\n{dots}<Class {aClass.__name__}, address: {id(aClass)}:\n{here}{above}{dots}>\n>'

    def __str__(self):
        self.__visited = {}
        here = self.__attrnames(self, 0)
        above = self.__listclass(self.__class__, 4)
        return f'<Instance of {self.__class__.__name__}, {id(self)}:\n{here}{above}>'


if __name__ == '__main__':
    import testmixin
    testmixin.tester(ListTree)
