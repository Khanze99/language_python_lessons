

class ListInherited:
    def __attrnames(self, indent=' ' * 4):
        result = f'Unders{"-" * 77}\n{indent} : \nOthers{"-" * 77}\n'
        unders = []

        for attr in dir(self):
            if attr[:2] == '__' and attr[-2:] == '__':
                unders.append(attr)
            else:
                result += f'\t{attr}={getattr(self, attr)}\n'
        return result.replace(':', ', '.join(unders))

    def __str__(self):
        return f'<Instance of {self.__class__.__name__}, address {id(self)}\n{self.__attrnames()}>'


if __name__ == '__main__':
    import testmixin
    testmixin.tester(ListInherited)