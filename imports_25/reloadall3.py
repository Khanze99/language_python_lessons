import types
from imp import reload
from reloadall import status, tryreload, tester


def transitive_reload(modules, visited):
    while modules:
        next_ = modules.pop()
        status(next_)
        tryreload(next_)
        visited.add(next_)
        modules.extend(x for x in next_.__dict__.values() if type(x) == types.ModuleType and x not in visited)


def reload_all(*modules):
    transitive_reload(list(modules), set())


if __name__ == '__main__':
    tester(reload_all, 'reloadall3')
