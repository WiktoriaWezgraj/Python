'''1. In every programming language there is a function to take input from the user. The function allows the program to pause and wait for the user to type something on the keyboard. Whatever the user types is captured as a string.

    Complete the following program code:'''

    # A program that reads your first and last name from the keyboard.
    # Store this data in two separate variables.
    # Then, print your full name i.e. first and last name separated by a single space.
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
full_name = first_name + ' ' + last_name
print(f'Your first name is {first_name} and your last name is {last_name}')
print(f'And your full name is {full_name}')