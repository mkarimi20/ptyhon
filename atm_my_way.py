
print("\nPlease select your choice from the following options: \n\t 1) Balance \n\t 2) withdraw \n\t 3) Deposit \n\t 4) Quit")
input_action = int(input("Enter your selected number: "))
currnet_balance = 850

if input_action == 1:
    print('Your currnet balance is $', + currnet_balance)
elif input_action == 2:
    withdraw = float(input('How much do you want to withdraw: '))
    print('$', currnet_balance-withdraw)
elif input_action == 3:
    deposit = float(input('How much do you want to add: '))
    print('$', deposit+currnet_balance)
else:
    exit