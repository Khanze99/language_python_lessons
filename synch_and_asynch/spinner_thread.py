import threading
import itertools
import time
import sys


class Signal:  # Этот класс определяет простой изменяемый объект с атрибутом go, который понадобится для управдения
    # потоком извне
    go = True


def spin(msg, signal):  # Эта функция буде выполняться в отдельном потоке. Аргумент signal - экземпляр определенного
    # выше класса Signal
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):  # бесконечный цикл, потому что функция itertools.cycle перепирает заданную
        # последовательность по кругу
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))  # Хитрость, позволяющая выполнить анимацию в тестовом режиме: возвращаем курсор
        # назад, печатая символы забоя (\x08)
        time.sleep(.1)
        if not signal.go:  # Если атрибут go не равен True, выходим из цикла
            break
    write(' ' * len(status) + '\x08' * len(status))  # Очищаем строку состояния, затирая ее пробелами и возвращая
    # курсор в начало


def slow_function():  # Допустим, что здесь происходит какое-то долгое вычесление
    # имитируем ожидание завершения длительной операции ввода-вывода
    time.sleep(3)  # Вызов sleep блокирует главный поток, но - и это очень важно - GIL освобождается,
    # так что второй поток может работать дальше
    return 42


def supervisor():  # Эта функция настраивает второй поток, отображает объект потока, выполняет долгое вычесление
    # и завершаем поток
    signal = Signal()
    spinner = threading.Thread(target=spin, args=('thinking!', signal))
    print('spinner object:', spinner)  # отображаем объекто второго потока. Вывод имеет вид <Thread(Thread-1, initial)>
    spinner.start()  # Запускаем второй поток
    result = slow_function()  # Вызываем, при этом главнй поток блокируется. А тем временем индикатор анимируется
    # вторым потоком
    signal.go = False  # Изменяем состояние signal; тем самым мы завершаем цикл for внутри функции spin
    spinner.join()  # Ждем завершения потока spinner
    return result


def main():
    result = supervisor()  # Вызываем функцию
    print('Answer:', result)


if __name__ == '__main__':
    main()
