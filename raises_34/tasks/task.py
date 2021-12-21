import sys
sys.path += ['/home/akhamidov/PycharmProjects/language_python_lessons/raises_34/tasks/']

from exctools import safe


class MyError(Exception): pass


@safe
def oops(): raise MyError('SPAM!')


if __name__ == '__main__':
    oops()