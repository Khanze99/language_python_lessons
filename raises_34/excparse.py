

class FormatError(Exception):
    logfile = 'formaterror.txt'

    def __init__(self, line, file):
        self.line = line
        self.file = file

    def logerror(self):
        log = open(self.logfile, 'a')
        print(f'Error at: {self.line} {self.file}', file=log)


def parser():
    raise FormatError(432, 'spam.xytx')


if __name__ == '__main__':
    try:
        parser()
    except FormatError as exc:
        exc.logerror()
