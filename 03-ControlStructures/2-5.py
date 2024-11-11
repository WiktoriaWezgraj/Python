'''5. Write a program that calculates and prints the quarter of the year for a given month number (1..12). Then check the program's results for the months:

    12, 10, 9, 1'''

    ###
    # Calculates and prints the quarter of the year for a given
    # month number (1..12)
    #
month = int(input('Enter month number (1..12): '))

if month >= 10:
    quarter = 4
elif 1 <= month <= 3 :
    quarter = 1
elif 4 <= month <= 6:
    quarter = 2
elif 7 <= month <= 9:
    quarter = 3
else:
    print('Invalid month')

print(f'Month {month} is in quarter {quarter}')