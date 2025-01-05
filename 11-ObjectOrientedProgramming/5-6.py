'''The bank account has a 26-digit number assigned when creating an account. 
The initial account balance is PLN 0. You can deposit any amount on the account. 
You can also withdraw any amount from the account, provided that it does not exceed the account balance. 
If you try to withdraw a larger amount, the following message will be displayed: "Insufficient funds on the account". 
At any time, it is possible to display information about the number and balance of the bank account in the following format:

Bank Account No: 11 1111 1111 1111 1111 1111 1111
Balance: PLN 25,38
Create a program that handles the bank account.

Familiarises yourself with a problem.
Identify an object
Define the states and behaviors of the object.
Transform the states and behaviors of the object into the fields and methods of the class that will serve as a pattern for creating an object.
Create a sketch of the class without creating any method content.
Create the content of each method.
Then, use the program and:

Create a bank account with the number 12 3456 5555 9090 1111 0000 7722
Display account balance
Deposit PLN 25,30
Display account balance
Withdraw PLN 31,70
Display account balance
Withdraw PLN 14
Display account balance'''

class Account:
    def __init__(self, number):
        self.number = number
        self.balance = 0
    def deposit(self, amount1):
        self.balance += amount1
    def withdraw(self,amount2):
        if self.balance - amount2 >= 0:
            self.balance -= amount2
        else:
            print('Insufficient funds on the account')
    def display(self):
        print(self.balance)


acc = Account('12 3456 5555 9090 1111 0000 7722')
acc.display()
acc.deposit(25.3)
acc.display()
acc.withdraw(31.70)
acc.display()