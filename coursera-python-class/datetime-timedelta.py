#In this first part of the first programming assignment, you should

#1.Write a program that reads in a number and prints the date that 
# number of days from now in this format: Saturday, February 06, 2021.

from datetime import datetime, timedelta
x = int(input())
y = datetime.now() + timedelta(days=x)
print( y.strftime("%A, %B %d, %Y"))