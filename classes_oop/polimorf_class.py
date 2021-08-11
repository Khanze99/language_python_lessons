

class Employee:
    def computeSalary(self): ...
    def giveRaise(self): ...
    def promote(self): ...
    def retire(self): ...


class Engineer(Employee):
    def computeSalary(self): ...


bob = Employee()
sue = Employee()
tom = Engineer()


company = [bob, sue, tom]
for emp in company:
    print(emp.computeSalary())
