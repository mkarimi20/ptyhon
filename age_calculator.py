import datetime
name = (input("enter your name: "))
age = (input("enter your current age: "))
now = datetime.datetime.now()

year = str((int(now.year) - int(age))+100)
print(name + ", you will be 100 years old in the year " + year)




