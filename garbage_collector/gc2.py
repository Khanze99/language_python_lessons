import gc
import pprint


class LinkedList:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def set_next(self, value):
        print(f'Linking nodes {self}.next = {value}')
        self.next = value

    def __repr__(self):
        return f'{self.__class__.__name__}({self.value})'


if __name__ == '__main__':

    a = LinkedList('1')
    b = LinkedList('2')
    c = LinkedList('3')

    a.set_next(b)
    b.set_next(c)
    c.set_next(a)

    a = b = c = None

    for i in range(2):
        print(f'Collecting {i:d} ...')
        n = gc.collect()
        print('Unreachable objects:', n)
        print('Remaining Garbage', pprint.pprint(gc.garbage))
