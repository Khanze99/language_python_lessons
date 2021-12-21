class MyError(Exception): pass


def stuff(file):
    raise MyError()


file = open('data', 'w')

try:
    stuff(file)
finally:
    file.close()
    print('close file')


print('not reached')
