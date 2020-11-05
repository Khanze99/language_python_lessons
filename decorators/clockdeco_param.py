import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


def clock(fmt=DEFAULT_FMT):  # наша фабрика параметризованных декораторов
    def decorate(func):  # это собственно декоратор
        def clocked(*_args):  # обертывает декорированную функцию
            t0 = time.time()
            _result = func(*_args)  # результат, возвращенный декорированной функцией
            elapsed = time.time() - t0
            name = func.__name__
            args = ', '.join((repr(arg) for arg in _args))  # В _args хранятся фактические аргументы clocked, тогда
            # как args - отображаемая строка
            result = repr(_result)  # строковое представление _result, предназначенное для отображения
            print(fmt.format(**locals()))  # использование **locals() позволяет ссылаться в fmt на любую локальную
            # переменную clocked
            return _result  # clocked заменяет декорированную функцию, поэтому должна возвращать то, что вернула бы эта
            # функция в отсутствие декоратора
        return clocked  # decorate возвращает clocked
    return decorate  # clock возвращает decorate


if __name__ == '__main__':

    @clock()  # clock() вызывается без аргументов, поэтому декоратор будет использовать форматную строку по умолчанию
    def snooze(seconds):
        time.sleep(seconds)

    for i in range(3):
        snooze(.123)
