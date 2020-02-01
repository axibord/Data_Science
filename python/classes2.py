# why use classes ( OOP ) : allow us tp group data and funtions and build on top of them with methods

import datetime


class Employee:

    RAISE_AMOUNT = 1.04
    num_employes = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.num_employes += 1  # we can use self but class name is better here

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


emp1 = Employee("Aghiles", "Schafer", 40000)
emp2 = Employee("moh", "lbilot", 100000)

my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))
