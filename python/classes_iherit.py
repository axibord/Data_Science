# why use classes ( OOP ) : allow us tp group data and funtions and build on top of them with methods


class Employee:

    RAISE_AMOUNT = 1.04
    num_employes = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_employes += 1  # this will run everytime we create new employee (object) we can use self but class name is better here

    def fullname(self):
        return "this is: {} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.RAISE_AMOUNT)

    @classmethod  # create methods to interacate with the constants
    def set_raise_amt(
        cls, amount
    ):  # cls remplace name of the calsse here its: Employee
        cls.RAISE_AMOUNT = amount

    @classmethod
    def from_string(cls, emp_str):  # cls remplace name of the calsse here its: Employee
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod  # static methods dont take self or cls as first argument
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(
    Employee
):  # by passing Employee we iherited everything from EMployee class
    RAISE_AMOUNT = 4

    def __init__(self, first, last, pay, langage):
        super().__init__(first, last, pay)
        self.langage = langage


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("--->", emp.fullname())


emp1 = Employee("Aghiles", "Schafer", 40000)
emp2 = Employee("moh", "lbilot", 100000)

dev1 = Developer("ghiles", "zenda", 3000, "C")
dev2 = Developer("sidoo", "smartguy", 100000000, "Python")

print(emp1.email)
print(emp2.email)
print(dev1.langage)
print(dev2.langage)

manager1 = Manager("Sue", "Smith", 90000, [dev1])
manager1.add_emp(dev2)
manager1.remove_emp(dev1)

manager1.print_emp()

print(
    isinstance(manager1, Employee)
)  # just to understand and experiment with inheritance
print(issubclass(Manager, Employee))
