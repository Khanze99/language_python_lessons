
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


class U1Ops:

    def op1(self):
        pass


class U2Ops:

    def op2(self):
        pass


class U3Ops:

    def op3(self):
        pass


class OPS(U1Ops, U2Ops, U3Ops):
    pass


ops = OPS()
user1 = User1(ops)
user2 = User2(ops)
user3 = User3(ops)
