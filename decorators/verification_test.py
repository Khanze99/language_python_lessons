from check import rangetest, typetest, valuetest


@typetest(a=str, b=int)
def spam(a, b):
    print(a, b)


spam('as', b=2)


@rangetest(percent=(0.0, 1.0))
def giveRaise(a, b, percent):
    print(a, b, percent)


giveRaise(1, 'asd', percent=0.50)
giveRaise(1, 'asd', 0.50)
# giveRaise(1, 'asd', 1.50)
# giveRaise(1, 'asd', percent=1.50)


@valuetest(a=str.islower, b=str.isdigit)
def foo(a, b):
    print(a, b)


foo('asdas', '123')