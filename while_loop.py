# count = 0
# while(count < 9):
#     print('the count it: ', count)
#     count = count+1

# print('Out of loop')


# The Infinite Loop
# A loop becomes infinite loop if a condition never becomes FALSE. You must be cautious
# when using while loops because of the possibility that this condition never resolves to a
# FALSE value. This results in a loop that never ends. Such a loop is called an infinite loop.


# count = 0
# while count < 10:
#     print(count, 'the number is less than 10')
#     count = count + 1   # what if we remove this line?
# else:
#     print(count, " is not less than 10")


# i = 1
# while i < 6:
#     print(i)
#     if (i == 3):
#         break
#     i += 1


# With the continue statement we can stop the current iteration, and continue with the next:
# i = 1
# while i < 6:
#     i += 1
#     if(i == 3):
#         continue
#     print(i)
# else:
#     pass

# i = 1
# while i < 6:
#     print(i)
#     i += 1
# else:
#     print("i is no longer less than 6")


# flag = 1
# while (flag):
#     print('Given flag is really true!')   # Guess what happens?
# print("Good bye!")


#  nested loops
# while expression:
#     while expression:
#         statement(s)
#     statement(s)

# for i in range(1, 11):
#     for j in range(1, 11):
#         k = i*j
#         print(k, end=' ')
# print('out of four loops')