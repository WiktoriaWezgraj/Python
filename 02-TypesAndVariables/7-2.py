'''2. The password is valid if it is at least 8 characters long. Write a program that checks whether the password length read from the keyboard is correct. 
Then, check if the program works correctly for the following passwords:

    university, peter123, (passwords ok)
    seven, anna333 (passwords to short)'''

    ###
    # A program that checks whether the password length
    # read from the keyboard is correct.
    #
password = input('Enter password: ')
password_ok = len(password) >= 8
print(f'Password length is valid: {password_ok}')