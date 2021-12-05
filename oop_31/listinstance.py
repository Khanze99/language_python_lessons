

class ListInstance:
    def __attrnames(self):
        result = ''

        for attr in sorted(self.__dict__):
            result+= f'\t{attr}={self.__dict__[attr]}\n'

        return result

    def __str__(self):
        return f'<Instance of {self.__class__.__name__}, address {id(self)}:\n{self.__attrnames()}>'
