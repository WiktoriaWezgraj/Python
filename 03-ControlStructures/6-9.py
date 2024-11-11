'''9. Write a program that calculates a dog\'s age in dog's years. For the first two years, a dog\'s life is equal to 10.5 human years. 
After that, each dog year is equal to 4 human years. Sample result:

    Enter the dog\'s age in human years: 15\
    The dog\'s age in dog's years is 73 years.'''

human_years=int(input("Enter dog's age in human years:"))

if human_years <= 2:
    dogs_age = human_years *10.5
else:
    dogs_age = (2*10.5) + (human_years-2) * 4


print(dogs_age)