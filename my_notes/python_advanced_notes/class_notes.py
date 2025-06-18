#class
#def init
#fullname
#raise amount, pay_rise, class method for raise use 3 payrates using class, classmethod and instance
#num of emp : names, pays with raise, no of employees
#class method
# emp_str_1 = 'Nish-Parajuli-100'
#class method for workday
#static method
#new subclass called manager with employees attr
#repr and str method for objects
#property, .setter and .deleter decorators



















class Employee:
    raise_amount = 1.04
    num_of_emps = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@mycompany.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_working(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

class Manager(Employee):

    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def del_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)


    def print_emp(self):
        emp_list = [emp.fullname() for emp in self.employees]
        emp_list.insert(0, 'no_of_emps_under = ' + str(len(emp_list)))
        print(emp_list)



import datetime
my_date = datetime.date(2024, 4, 13)

emp_1 = Employee('Nish', 'Parajuli', 100000)
emp_2 = Employee('Dylan', 'Bob', 200000)

emp_str_3 = 'John-Doe-70000'
emp_str_4 = 'Steve-Smith-30000'
emp_str_5 = 'Jana-Doe-90000'

emp_3 = Employee.from_string(emp_str_3)

emp_1.raise_amount = 1.05
emp_2.set_raise_amt(1.01)
emp_1.apply_raise()
emp_2.apply_raise()

print(Employee.fullname(emp_1))
print(emp_2.fullname())
print(emp_3.fullname())
print(emp_1.email)
print(emp_1.pay)
print(emp_2.pay)
print(Employee.num_of_emps)
print(Employee.is_working(my_date))
print(emp_1)

man_1 = Manager('Albert', 'Einstein', '200', [emp_3])
man_1.add_emp(emp_1)
man_1.add_emp(emp_2)
man_1.del_emp(emp_3)
print(man_1.fullname())
man_1.print_emp()

































