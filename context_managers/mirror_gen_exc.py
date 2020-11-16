import contextlib


@contextlib.contextmanager
def looking_glass():
    import sys
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    msg = ''  # переменная для хранения возможного сообщения об ошибке

    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:  # Обработка исключения, устанавливаем сообщение об ошибке
        msg = 'Пожулайсту, НЕ НАДО делить на нуль!'
    finally:
        sys.stdout.write = original_write  # восстанавливаем исходный метод

        if msg:
            print(msg)  # Отображаем сообщение об ошибке, если оно не пусто
