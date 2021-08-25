import builtins


def makeopen(name):
    original = builtins.open

    def custom(*args, **kwargs):
        print('Custom open call %r:' % name, *args, **kwargs)
        return original(*args, **kwargs)

    builtins.open = custom
