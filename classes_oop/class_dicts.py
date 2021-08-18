

rec = ('Bob', 40.5, ['dev', 'mgr'])
print(rec[0])

rec = {}
rec['name'] = 'Bob'
rec['age'] = 40.5
rec['jobs'] = ['dev', 'mgr']
print(rec['name'])


class rec: pass


rec.name = 'Bob'
rec.age = 40.5
rec.jobs = ['dev', 'mgr']
print(rec.name)

pers1 = rec()
pers1.name = 'Bob'
pers1.jobs = ['dev', 'mgr']
pers1.age = 40.5

pers2 = rec()
pers2.name = 'Sue'
pers2.jobs = ['dev', 'cto']

print(pers1.name, pers2.name)


class Person:
    def __init__(self, name, jobs: list, age=None):
        self.name = name
        self.jobs = jobs
        self.age = age

    def info(self):
        return self.name, self.jobs


rec1 = Person('Bob', ['dev', 'mgr'], 40.5)
rec2 = Person('Sue', ['dev', 'cto'])

print(rec1.jobs)
print(rec2.info())
