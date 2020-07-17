class Employee:
    
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'
        
        Employee.num_of_emps +=1

    
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
       
    
    def apply_raise(self):
        self.pay = int(self.pay * 1.04)
    
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount
    
    
    
    @classmethod
    def from_string(cls,emp_str):
        first,last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workingday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True








emp_1 = Employee('Fahim','Arman', 50000)
emp_2 = Employee('Corey', 'Schafer', 60000)

#emp_1.fullname()
#emp_2.fullname()

Employee.set_raise_amount(1.1)

print(Employee.fullname(emp_1))
print(Employee.fullname(emp_2))

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(emp_1.__dict__)

emp_1.raise_amount = 1.05

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(emp_1.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

print(Employee.num_of_emps)

print('.' * 25)

emp_str_1 = 'john-doe-70000'
new_emp_1 = Employee.from_string(emp_str_1)

print('|| ' + new_emp_1.email + ' ||')

print('.' * 25)

print(Employee.num_of_emps)


print('.' * 25)
print('.' * 25)
print('.' * 25)

import datetime

my_date = datetime.date(2016,7,10)

print(Employee.is_workingday(my_date))



