

def tester(start):
    state = start

    def nested(label):
        st = 0
        print(label, st)

        def n2():
            nonlocal state
            print(state)
            state += 1
        n2()
    return nested
