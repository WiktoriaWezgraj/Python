'''19. Write a program that converts a decimal number into a binary number. To convert a decimal number to binary, follow these steps:

    1. Read a decimal number from the keyboard.
    1. Divide the number by 2 and note the remainder.
    1. Divide the quotient obtained by 2 and note the remainder.
    1. Repeat the same process till we get 0 as the quotient.
    1. Write the values of all the remainders starting from the bottom to the top. That will be the required binary number.

    Sample result:

    Enter decimal number: 12\
    12(10) = 1100(2)'''

decimal = int(input('Decimal: '))
binary = ''
while decimal>0:
    remainder = decimal % 2
    binary = str(remainder) + binary
    decimal = decimal//2

print(binary)