
import sys


def bye():
    sys.exit(40)


try:
    bye()
except Exception:
    print('got it')

print('continuing')
