

registry = set()  # чтобы ускорить добавление и удаление функций
# set.discard - удаляет указанный элемент из множества, если он там присутсвует


def register(active=True):  # принимает необязательный именованный аргумент
    def decorate(func):  # собственно декоратором является внутренняя функция decorate, она принимает аргумента функцию
        print('running register(active=%s) -> decorate(%s)'
              % (active, func))

        if active:  # регистрируем func, только если аргумент active(определенный в замыкании) равен True
            registry.add(func)
        else:
            registry.discard(func)  # Если not active и функция func присутствует в registry, удаляем ее

        return func  # Поскольку decorate - декоратор, он должен возвращать функцию
    return decorate  # функция register - наша фабрика декораторов, поэтому она возвращает decorate


@register(active=False)  # фабрику @register следует вызывать как функцию, передавая ей нужные параметры
def f1():
    print('running f1()')


@register()  # Даже если параметров нет, register все равно нужно вызывать как функцию - @register() - чтобы она
# вернула настоящий декоратор decorate
def f2():
    print('running f2()')


def f3():
    print('running f3()')

# При импорте модуля -> import decorators.with_parameters
# running register(active=False) -> decorate(<function f1 at 0x7f62a509c050>)
# running register(active=True) -> decorate(<function f2 at 0x7f62a509c0e0>)
# >>> import decorators.with_parameters as wp
# >>> wp.registry
# {<function f2 at 0x7f62a509c0e0>}
