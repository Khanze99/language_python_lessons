

class Traceback:
    def message(self, arg):
        print('running' + arg)

    def __enter__(self):
        print('starting with block')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print('exited normally\n')
        else:
            print('raise an exception! ' + str(exc_type))
            return False


if __name__ == '__main__':
    with Traceback() as action:
        action.message('1')
        print('reached')

    with Traceback() as action:
        action.message('test 2')
        raise TypeError
        print('not reached')
