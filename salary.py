name = (input("enter your name: "))
salary = (input("enter your currnt salary: "))


def salary_cal(salary):
    if salary is None:
        print(name, + ' your slary is $1000')
    
    elif int(salary) > 0:
        print(str(name) + " your slary is " + str(salary))
    
print(salary_cal(salary))
