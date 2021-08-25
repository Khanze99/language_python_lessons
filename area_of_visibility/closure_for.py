
def make_actions():
    acts = []
    for i in range(5):
        acts.append(lambda x: i ** x)

    return acts


acts = make_actions()
print(acts[0](2))  # 16
print(acts[1](2))  # 16
print(acts[2](2))  # 16
print(acts[4](2))  # 16


def make_actions1():
    acts = []
    for i in range(5):
        acts.append(lambda x, i=i: i ** x)

    return acts


acts = make_actions1()
print(acts[0](2))  # 0
print(acts[1](2))  # 1
print(acts[2](2))  # 4
print(acts[4](2))  # 16
