

class Spam:
    numInstance = 0

    def count(cls):
        cls.numInstance += 1

    def __init__(self):
        self.count()

    count = classmethod(count)

    # def printNumInstance(cls):
    #     print(f"Number of instances created: {cls.numInstance}, {cls}")

    # printNumInstance = classmethod(printNumInstance)


class Sub(Spam):
    numInstance = 0
    # def printNumInstance(cls):
    #     print("Extra stuff...", cls)
    #     Spam.printNumInstance()
    #
    # printNumInstance = classmethod(printNumInstance)
    def __init__(self):
        Spam.__init__(self)


class Other(Spam):
    numInstance = 0