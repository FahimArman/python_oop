class Employee:
    
    raise_amount = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'



class Developer(Employee):

    raise_amount = 1.10
    
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    
    def __init__(self,first,last,pay,employees = None):
        super().__init__(first,last,pay)
        
        if employees is None:
            self.employees =[]
        else:
            self.employees = employees


    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)


    def print_emps(self):
        for emp in self.employees:
            print ('-->', emp.email)




developer_01 = Developer('Fahim','Arman',50000,'Python')
developer_02 = Developer('John','Doe',60000,'Java')
developer_03 = Developer('Sue','Lang',50000,'C')
developer_04 = Developer('Joungue','Kim',60000,'C++')

print(developer_01.email)
print(developer_01.prog_lang)



mgr_1 = Manager('Sue','Smith', 90000,[developer_01])

mgr_1.add_emp(developer_02)
mgr_1.add_emp(developer_03)
mgr_1.add_emp(developer_04)

mgr_1.remove_emp(developer_01)
print('.' * 25)
print('.' * 25)
mgr_1.print_emps()






print(isinstance(mgr_1,Developer))
print(issubclass(Developer,Employee))





