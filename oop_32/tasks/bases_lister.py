from oop_31.lister import ListInstance


class ListSubBases(ListInstance):
    def __attrnames(self):
        result = ""

        for attr in sorted(self.__dict__):
            result += f"\t{attr}={self.__dict__[attr]}\n"

    def __str__(self):
        return f"<Instance of {self.__class__.__name__}({', '.join(klass.__name__ for klass in self.__class__.__bases__)}), " \
               f"address: {id(self)}:\n{self.__attrnames()}>"
