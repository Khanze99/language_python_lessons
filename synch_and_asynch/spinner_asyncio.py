import asyncio
import itertools
import sys


@asyncio.coroutine  # Сопрограммы, работающие с asyncio, должны быть снабжены декоратором @asyncio.coroutine. Это
# необязательно, но в высшей степени желательно.
def spin(msg):  # Здесь нам не нужен аргумент signal, который в функции spin из примера с потоком служил для
    # завершения потока
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            yield from asyncio.sleep(.1)  # Используем yield from asyncio.sleep(.1), а не просто time.sleep(.1),
            # чтобы спать, не блокируя цикл обработки событий
        except asyncio.CancelledError:  # Если после пробуждения spin возникло исключение, значит, была запрошена
            # отмена, поэтому выходим из цикла
            break

    write(' ' * len(status) + '\x08' * len(status))


@asyncio.coroutine
def slow_function():  # теперь сопрограмма, в которой yield from используется, чтобы цикл обработки событий мог
    # продолжать работу, пока сопрограмма спит, имитируя ввод-вывод
    """имитируем ожидание завершения длительной операции ввода-вывода"""
    yield from asyncio.sleep(3)  # это выражение уступает управление главному циклу, который возобновит сопрограмму
    # после указанной в sleep задержки
    return 42


@asyncio.coroutine
def supervisor():  # тоже сопрограмма, поэтому она может управлять функцией slow_function с помощью yield from
    spinner = asyncio.create_task(spin('thinking!'))  # планирует выполнение сопрограммы spin
    print('spinner object:', spinner)  # Распечатывает объект Task
    result = yield from slow_function()  # Управляем функцией. Когда она завершится, мы получим возвращенное значение.
    # А тем временем цикл обработки событий продолжает работать, потому что slow_function() уступила управление
    # главному циклу, выполнив yield from asyncio.sleep(3)
    spinner.cancel()  # Объект можно отменить. Возбуждается исключение asyncio.CancelledError в том выражении yield,
    # на котором сопрограмма приостановилась. Сопрограмма может перехватить это исключение и отложить отмену или даже
    # вовсе отказаться от нее
    return result


def main():
    loop = asyncio.get_event_loop()  # Получаем ссылку на цикл обработки событий
    result = loop.run_until_complete(supervisor())  # Управляем сопрограммой supervisor, пока она не завершится.
    # Значение, возвращенное сопрограммой, будет получено здесь
    loop.close()
    print('Answer:', result)


if __name__ == '__main__':
    main()
