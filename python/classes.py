# why use classes ( OOP ) : allow us tp group data and funtions and build on top of them with methods

class Employee:
    RAISE_AMOUNT = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
    
    def fullname(self):
        return 'this is: {} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.RAISE_AMOUNT)






emp1 = Employee("Aghiles", "Schafer", 40000)

print(emp1.email)

print(emp1.fullname())

print(Employee.fullname(emp1))

emp1.apply_raise()
print(emp1.pay)

print(emp1.RAISE_AMOUNT)
