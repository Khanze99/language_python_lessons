
import sys
print(sys.path)

from dualpkg import m1

def somefunc():
    m1.somefunc()
    print('m2.somefunc')

print(__name__)
if __name__ == '__main__':
    somefunc()