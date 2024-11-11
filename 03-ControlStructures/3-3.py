'''3. The discount is available to children under 18, or people 65 or older. Write a program that checks whether a person of a given age is eligible for the discount. 
Then use the program to check if people of the age listed below are eligible for a discount.

    72 (discount), 65 (discount), 64, 18, 17 (discount)'''

    ###
    # Checking if discount is available
    # The discount is available to children under 18,
    # or people 65 or older.
    #
age = int(input('Enter your age: '))

if age < 18 or age >= 65:
    print('Discount')
else:
    print('No discount')