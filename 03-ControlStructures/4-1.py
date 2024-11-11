'''1. Write a program that prints the name of university where you are studying with an extra space between characters (add a space between each character).
 Sample result:

    ```
    Krakow University of Economics
    K r a k o w   U n i v e r s i t y   o f   E c o n o m i c s'''

    ###
    # Prints the name of university where you are studying
    # with an extra space between characters (add a space between
    # each character)
    #
university = 'Krakow University of Economics'
university_expanded = ''

for char in university:
    university_expanded += char + " "

print(university_expanded)


   