import sys


def knights():
    title = 'Sir'
    action = lambda x: title + ' ' + x

    return action


act = knights()
msg = act('robin')
print(msg)


showall = lambda x: list(map(sys.stdout.write, x))
t = showall(['spam\n', 'toast\n', 'eggs\n'])