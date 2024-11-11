'''6. Write a program that asks the user for their age and then checks which age group they belong to:

    * Child: under 13
    * Teen: 13 to 19
    * Adult: 20 to 64
    * Senior: 65 or older'''

age = int(input('Whats your age?'))
if age < 13:
    print("Child")
elif 13 <= age <=  19:
    print("Teen")
elif 20 <= age <=64:
    print("Adult")
elif age>= 65:
    print("Senior")
else:
    print("Incorrect input")