

def f1():
    x = 88

    def f2(x=x):
        print(x)
    f2()


f1()
