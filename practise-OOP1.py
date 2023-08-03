class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{}{}.format(self.first, self.last)'
    
    def apply_raise(self):
        return '{}{}'.format(self.first, self.last)
    
class Developer(Employee):
    raise_amt = 1.10
    #instead of 2 new employees create 2 new developers
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []

        else:
            self.employees = employees

    """ adding employees """
    def add_emp(self, emp):
       if emp not in self.employees:
           self.employees.append(emp)

    """ remove employees """       
    def del_emp(self,emp):
        if emp not in self.employees:
            self.employees.remove(emp)

    """ print out all employees from list"""
    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname)




dev_1 = Developer('Corey', 'Schafer', '50000', 'Python')
dev_2 = Developer('Test', 'Employee', '60000', 'Java')

# print(help(Developer))
# print(dev_1.email)
# print(dev_2.prog_lang)



print(isinstance(dev_1, Employee))


