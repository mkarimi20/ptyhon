class ATM:
    print("\nPlease select your choice from the following options: \n\t 1) Balance \n\t 2) withdraw \n\t 3) Deposit \n\t 4) Quit")
    input_action = int(input("Enter your selected number: "))
    currnet_balance = 850

    def __init__(self, cash):
        self.cash = cash

    def balance(self):
        if self.input_action == 1:
            print(self.currnet_balance)

    def withdraw(self):
        if self.input_action == 2:
            withdraw_amount = float(input('How much do you want to withdraw: '))
            print(self.currnet_balance-withdraw_amount)

    def deposit(self):
        if self.input_action == 3:
            deposit_amount = float(input('How much do you want to add: '))
            print(self.currnet_balance+deposit_amount)
    
    def pay_bill(self):
        if self.input_action == 4:
            pay_amount = float(input('How much do you want to pay: '))
            print(self.currnet_balance-pay_amount)


user = ATM('Karimi')
if user.balance <= 1 :
    print(user.balance)
elif len(user.withdraw) > 0:
    print(user.withdraw)
elif len(user.deposit) > 0:
    print(user.deposit)
else:
    print(user.pay_bill)
# print(user.balance())
# print(user.withdraw())
# print(user.deposit())
# print(user.pay_bill())