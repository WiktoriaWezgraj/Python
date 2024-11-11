'''2. As you remember, the input() function allows you to read only a string from the keyboard. 
In the module keyboard.py, define your own functions that allow reading other types of data from the keyboard:

    * input_string() that returns a string entered from the keyboard
    * input_integer() that returns an integer number entered from the keyboard
    * input_real() that returns a real number entered from the keyboard
    * input_boolean() that returns a boolean value depending on the pressed y/n key'''

    ###
    # Functions to read any data type from the keyboard
    #
def input_string(message):
     = input(message)
    return ...

def input_integer(message):
    ... = input(message)
    return ...

def input_real(message):
    ... = input(message)
    return ...

def input_boolean(message):
    ... = input(message)
    return ...

# Then, write a program that allows you to enter and print employee data. Due to personal data protection, you can determine whether 
# information about the employee's salary will be printed.

#     ###
#     # Allows to enter and print employee data. Due to personal
#     # data protection, you can determine whether information about
#     # the employee's salary will be printed
#     #
#     import ...

#     # Reads employee's data from keyboard
#     first_name = input_string('Enter name: ')
#     last_name = ...
#     age = ...
#     salary = ...
#     is_salary_hidden = input_boolean('Hide salary? (y/n)')

#     # Prints employee's record
#     print('DATA RECORD')
#     print('===========')
#     print('Name:', ...)
#     print(...)
#     print(...)
#     if ...:
#         print('Salary')
#     ```