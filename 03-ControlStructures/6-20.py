'''20. There are coins of 1, 2 and 5 Polish Zlotys (PLN). 
Write a program showing any amount (natural number) read from the keyboard with as few coins as possible.

    Enter the amount in PLN: 18\
    The amount of PLN 18 in coins:\
    5 PLN coins: 3\
    2 PLN coins: 1\
    1 PLN coins: 1'''

amount = int(input('Enter the amount in PLN:'))
coins_5 = amount // 5
amount = amount % 5
coins_2 = amount // 2
amount = amount % 2
coins_1 = amount

print(coins_5, coins_2, coins_1)