'''1. The string type is a basic data type used to store sequences of characters such as letters, numbers, symbols, and special characters. 
It is one of the most commonly used data types that represents text and is extremely flexible. You can find out how many characters are in a string using the len() function.

Complete the program below to calculate the number of characters in your name and surname.'''

    ###
    # A program that calculates the number of characters
    # of your name, surname and full name
    #
name = 'Wiktoria'   # replace Anna with your name
surname = 'W' # replace May with your surname
characters_in_name = len(name)
print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {len(surname)} characters')
print(f'Your full name has {len(name + " " + surname)} characters') # with a space between name and surname