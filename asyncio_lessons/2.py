

def doubler():
    print('> Начало функции')
    value = 2 * (yield)
    print(f'> value {value}')
    yield value
    print('> Конец функции')


if __name__ == '__main__':

    d = doubler()
    next(d)

    res = d.send(21)
    print(res)
    print(d.send(res))