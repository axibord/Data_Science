class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property  # this proprety mean we can use the methods without the parentheses  and in the same time updating the email
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @property  # this proprety mean we can use the methods without the parentheses  and in the same time updating the email
    def email(self):
        return "{}.{}@gmail.com".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter  # to acces this deleter use : del object.fullname
    def fullname(self):
        print("Deleted Name !")
        self.first = None
        self.last = None


emp1 = Employee("Aghiles", "Lou")

emp1.first = "moh"

emp1.fullname = "just test"

print(emp1.first)
print(emp1.email)
print(emp1.fullname)

del emp1.fullname
