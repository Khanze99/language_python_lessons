

class OPS:
    def op1(self):
        pass

    def op2(self):
        pass

    def op3(self):
        pass


class User1:
    def __init__(self, ops):
        self.ops = ops

    def some_behavior(self):
        self.ops.op1()


class User2:
    def __init__(self, ops):
        self.ops = ops

    def some_behavior(self):
        self.ops.op2()


class User3:
    def __init__(self, ops):
        self.ops = ops

    def some_behavior(self):
        self.ops.op3()