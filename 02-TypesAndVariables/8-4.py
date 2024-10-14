'''4. A SWIFT code (also known as BIC - Bank Identifier Code) is a unique identification code used to identify a specific bank or financial institution globally. It is primarily used for international wire transfers and communication between banks.

    SWIFT code is typically 8 or 11 characters long and is composed of the following elements:

    * Bank Code (4 characters)
    * Country Code (2 characters)
    * Location Code (2 characters)
    * Branch Code (3 characters - optional)

    Write a program that reads a SWIFT code from the keyboard and prints the bank code and the country code. Then, use the program to print information for the following SWIFT codes:  
    BPKOPLPW, CHASUS33, DEUTDEFF.'''

    ###
    # A program that reads a SWIFT code from the keyboard
    # and prints the bank code and country code.
    #
swift = input('Enter code: ')
print(f'Bank Code: {swift[:4]}')
print('Country Code: ', swift[5:7])