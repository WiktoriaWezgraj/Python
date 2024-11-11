'''1. There are a number of built-in functions, ready to use, e.g. len(), print(), input() or type(). 

    Using built-in Python functions, write a program that calculates and prints:

    * the largest number: 7,5,6,3,8,2
    * the smallest number: 4,7,2,3,9,8
    * length of the phrase: \"computer science\"
    * letter read from the keyboard ---input()
    * number representing the string \"20303\" ---str(input())
    * binary string representing decimal number 304 ---bin(304)
    * hexadecimal string representing decimal number 304 ---hex(304)
    * integer representing the Unicode code of the € sign ---ord()
    * absolute value of -17 ---abs()''' 

    ###
    # Program for testing built-in functions
    #
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)