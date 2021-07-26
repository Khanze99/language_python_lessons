from typing import Optional

# Подклассы могли служить заменой для своих суперклассов


class Rectangle:
    def __init__(self):
        self._width = 0
        self._length = 0

    def set_width(self, width: int):
        self._width = width

    def set_length(self, length: int):
        self._length = length


class SquareR(Rectangle):
    """
    этот подкласс не может служить супер классу заменой
    поэтому это не подходит к принципу LSP
    лучше будет разделить эти классы от наследования
    """

    def set_width(self, width: int):
        self._width = width
        self.set_length(width)

    def set_length(self, length: int):
        self._length = length
        self.set_width(length)


class Square:
    def __init__(self):
        self._width: Optional[int] = 0

    def set_width(self, width: Optional[int]):
        self._width = width
