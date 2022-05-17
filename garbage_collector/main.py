import gc


gc.set_debug(True)
gc.disable()  # отключение сборщика


# ----------------------------------------------------------------------

class Track:
    def __init__(self):  # конструктор
        print("Intitialisting your object here")

    def __del__(self):  # деструктор
        print("Deleting and clearing your object here")


def tracker():
    print('A')
    A = Track()
    print('B')
    B = Track()

    print('Deleting here ...')

    del A
    del B


    gc.collect()  # гарантирует, что сборщик мусора освободит пространство памяти,
    # занимаемое объектами A и B


# ----------------------------------------------------------------------


class User:

    def __init__(self, count):
        self.count = count

    def __str__(self):
        return f'User{self.count}'

    def __del__(self):
        print(f"No reference left for {self}")


if __name__ == '__main__':
    user1 = User(1)
    user2 = user1
    user3 = user1

    user1 = None
    user2 = None
    user3 = None
