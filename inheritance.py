class Employee():
    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
        Employee.num_of_employees += 1

    def fullname(self):
        # what if we select emp_1.first
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)


emp_1 = Employee('Asad', 'Saad', 400)
emp_2 = Employee('Ali', 'Jafar', 600)

print('Employee salary : ', emp_1.pay)

emp_1.apply_raise()
print('Employee salary after raise: ', emp_1.pay)


class accounting(Employee):
    raise_amount = 2
print('this is a subclass and only for acounting')
acc1 = accounting('ali', 'saberi', 433)
acc2 = accounting('jaber', 'aziz', 3324)

print(acc1.first, acc1.pay)