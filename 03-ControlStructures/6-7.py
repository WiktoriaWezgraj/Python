'''7. Write a program that checks that both people are adults. Read
    people's data from the keyboard.'''

    ###
    # Checking if both people are adults
    #
person1_name = input('Enter first person name: ')
person1_age = int(input('Enter first person age: '))
person2_name = input('Enter second person name: ')
person2_age = int(input('Enter second person age: '))
if person1_age >= 18 and person2_age >= 18:
    print('Both {person1_name} and {person2_name} are adults')
else:
    print('Either {person1_name} or {person2_name} is not an adult')