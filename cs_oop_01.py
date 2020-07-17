

class Employee:

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)


emp_1 = Employee('Fahim','Arman', 50000)
emp_2 = Employee('Corey', 'Schafer', 60000)

#emp_1.fullname()
#emp_2.fullname()

print(Employee.fullname(emp_1))
print(Employee.fullname(emp_2))











