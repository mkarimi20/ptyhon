

#num = range(1, 16 + 1)
counter_even = 0
counter_odd = 0

for x in range(1, 101):
    if not x % 2:
        counter_even += 1
    else:
        counter_odd += 1
print("there are" , counter_odd , "odd numbers")
print("there are" , counter_even , "odd numbers")
