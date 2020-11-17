from collections import namedtuple

Result = namedtuple('Result', 'count average')


# субгенератор
def averager():
    total = 0
    count = 0
    average = None

    while True:
        term = yield

        if term is None:
            break  # Чтобы вернуть значение, сопрограмма должна завершиться нормально, поэтому проверяется условие
            # выхода из цикла подсчета среднего

        total += term
        count += 1
        average = total / count

    return Result(count, average)  # Возвращаем именованный кортеж, содержащий count и average


# делегирующий генератор
def grouper(results, key):
    while True:  # на каждой итерации этого цикла создается новый экземпляр averager; каждый из них является
        # объектом - гегератором, работающим как сопрограмма
        results[key] = yield from averager()  # Значение, отправляемое генератору grouper, помешается выражением
        # yield from в канал, открытый с объектом averager.grouper остается приостановленным, пока averager потребляет
        # значения, отправляемые клиентом. Когда выполнение averager завершится, возвращенное им значение будет связано
        # с results[key]. После этого в цикле while создается очередной экземпляр averager для потребления
        # последующих значений


# client
def main(data):
    results = {}
    for key, values in data.items():
        group = grouper(results, key)  # объект - генератор, получающийся в результаты вызова grouper с аргументами
        # results - словарем, в котором будут собираться результаты, - и key - конкретным ключом этого словаря.
        # Этот объект будет работать как сопрограмма
        next(group)  # Инициализируем сопрограмму

        for value in values:
            group.send(value)

        group.send(None)
        print(results)
        report(results)


# вывод отчета
def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:2f}{}'.format(
            result.count, group,
            result.average, unit
        ))


data = {
 'girls;kg':
 [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
 'girls;m':
 [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
 'boys;kg':
 [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
 'boys;m':
 [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}

if __name__ == '__main__':
    main(data)