'''4. A payment terminal in a store allows card payments. The customer has money in his bank account. 
The total value of purchases is given. The terminal prints a message whether the payment can be made or whether there are no funds in the customer's bank account. 
Write a program that acts as a payment terminal. Then, use the program and pay for the purchases below.

    140, 499, 500, 501, 720 (for the last two amounts, there are no funds)'''

    ###
    # Credit card payment 
    #
account_balance = 500
total_payment = float(input("Enter a payment: "))
    
if total_payment <= account_balance:
    print('Payment completed')
else:
    print('No funds')
