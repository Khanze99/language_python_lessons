

def loadclass():
    import sys, importlib
    module_name = sys.argv[1]
    module = importlib.import_module(module_name)

    print(f'[Using: {module.CardHolder}]')
    return module.CardHolder


def print_holder(who):
    print(who.acct, who.name, who.age, who.remain, who.addr, sep=' / ')


if __name__ == '__main__':
    CardHolder = loadclass()
    bob = CardHolder('1234-5678', 'Bob Smith', 40, '123 main st')
    print_holder(bob)

    bob.name = 'Bob Q. Smith'
    bob.age = 50
    bob.acct = '23-45-67-89'
    print_holder(bob)

    sue = CardHolder('5678-12-34', 'Sue Jones', 35, '124 main stk')
    print_holder(sue)

    try:
        sue.age = 200
    except ValueError:
        print('Bad age for Sue')

    try:
        sue.remain = 5
    except:
        print("Can't set sue.remain")

    try:
        sue.acct = '1234567'
    except:
        print('Bad acct for Sue')
