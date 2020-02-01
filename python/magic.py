class Employee:

    RAISE_AMOUNT = 1.04
    num_employes = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
        Employee.num_employes += 1  # this will run everytime we create new employee (object) we can use self but class name is better here


    def __repr__(self): #good habit for professional use ( representation of the class)
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    #def __str__(self):
    #    return '{} - {}'.format(self.fullname(), self.email)
    
    def __add__(self, self2): # magic method that allow us to use something like: print(emp1 + emp2)
        return self.pay + self2.pay
    
    def __len__(self): #allow us to calc tje length and print it later when we want
        return len(self.fullname())
       
    def fullname(self):
        return 'this is: {} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.RAISE_AMOUNT)

    
    @classmethod # create methods to interacate with the constants 
    def set_raise_amt(cls, amount):   # cls remplace name of the calsse here its: Employee
        cls.RAISE_AMOUNT = amount
    
    @classmethod
    def from_string(cls, emp_str):    # cls remplace name of the calsse here its: Employee
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod   # static methods dont take self or cls as first argument
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp1 = Employee('Aghilese','Lou',5000)
emp2 = Employee('sidoo','martguy',100000)

print(emp1)
print(emp1 + emp2)

print(len(emp1))
