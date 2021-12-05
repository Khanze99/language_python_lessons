

class Methods:
    def imeth(self, x):
            print([self, x])

    @staticmethod
    def smeth(x):
        print([x])

    @classmethod
    def cmeth(cls, x):
        print([cls, x])

    @property
    def name(self):
        return f"Bob " + self.__class__.__name__

