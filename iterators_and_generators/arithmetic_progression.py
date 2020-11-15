

class ArithmeticProgression:

    def __init__(self, begin, step, end=None):  # требует двух аргументов, аргумент end необязательный, если равен None
        self.begin = begin
        self.step = step
        self.end = end  # None -> бесконечный ряд

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)  # эта строка порождает значение, равное self.begin, но
        # приведенное к типу последующих слагаемых
        forever = self.end is None  # флаг, который равен True, если атрибут end равен None, в этом случае порождается
        # неограниченный ряд
        index = 0
        while forever or result < self.end:  # этот цикл продолжается вечно или пока значение result не окажется больше
            # или равно self.end. По выходе из цикла завершается и функция
            yield result  # Генерируется текущее значение result
            index += 1
            result = self.begin + self.step * index  # Вычисляется следующий потенциальный результат. Возможно,
            # он никогда не будет отдан, потому что цикл while завершится раньше

