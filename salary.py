name = str(input("enter your name: "))
salary = input("enter your currnt salary: ")


def salary_cal(salary):
    if len(salary) < 1:
        print(str(name) + ' your slary is $1000')
    
    elif salary is not None and int(salary) > 0:
        print(str(name) + " your slary is " + str(salary))
    
salary_cal(salary)