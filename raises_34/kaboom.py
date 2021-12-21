

def kaboom(x, y):
    print(x + y)


try:
    kaboom([1, 2], 'as')
except TypeError:
    print('Hello world')

print('resuming here')
