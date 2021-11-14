from abc import ABCMeta, abstractclassmethod


class Super(metaclass=ABCMeta):

    @abstractclassmethod
    def method(self):
        pass
