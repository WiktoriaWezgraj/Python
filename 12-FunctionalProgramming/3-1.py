'''The report below shows the last five credit card payments in Euro:

15.90
38.47
4.07
132.70
9.15
Write a program that calculates and displays transaction amounts in Polish zlotys (1 EUR = 4.5 PLN). Use anonymous and map() functions. Sample result:

71.55
173.11
18.31
597.15
41.17
transactions_in_eur = [15.90,38.47,4.07,132.70,9.15]
transactions_in_pln = list(map(lambda x:x*4.5, transactions_in_eur))
# print pln list ...'''

transactions_in_eur = [15.90,38.47,4.07,132.70,9.15]
transactions_in_pln = list(map(lambda x:x*4.5, transactions_in_eur))
# print pln list ...
print(transactions_in_pln)