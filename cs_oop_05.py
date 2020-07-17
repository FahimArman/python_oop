

class Employee:
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def __repr__(self):
        return '{},{},{},{} --> {}'.format(self.first,self.last,self.pay,self.fullname(),self.email)

    def __str__(self):
        return '{} --> {}'.format(self.fullname(),self.email)

    
    def __add__(self,other):
        return self.pay + other.pay






emp_1 = Employee('Fahim', 'Arman', 50000)
emp_2 = Employee('Jack','Lee', 60000)

print('.' * 25)
print('.' * 25)

print(emp_1)
print(repr(emp_1))
print(str(emp_1))

print(emp_1.__repr__())
print(emp_1.__str__())


print('.' * 25)
print('.' * 25)


print(emp_1+emp_2)


