
class LookingGlass:

    def __enter__(self):  # Python вызывает метод с ожним лишь аргументом self
        import sys

        self.original_write = sys.stdout.write  # Текущий метод сохраняется в атрибуте экземпляра для последующего
        # использования
        sys.stdout.write = self.reverse_write  # Подменяем своим собственным методом
        return 'JABBERWOCKY'  # Возвращаем строку, просто чтобы поместить что-то в переменную what

    def reverse_write(self, text):  # Наш метод инвертирует переданный аргумент text и вызывает сохраненную реализацию
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_val, traceback):  # вызывает метод с аргументами None .. None, если не было ошибок;
        # если же имело место исключение, то в аргументах передаются данные об исключении, описанные ниже
        import sys  # Повторный импорт модулей обходится дешево, потому что Python их кеширует
        sys.stdout.write = self.original_write  # Восстанавливаем исходный метод
        if exc_type is ZeroDivisionError:  # Если было исключение, то печатаем ...
            print('Пожалуйста, НЕ НАДО делить на нуль!')
            return True  # Если метод возвращает None или вообще что-нибудь, кроме True, то исключение, возникшее внутри
            # блока with, распростроняется дальше
