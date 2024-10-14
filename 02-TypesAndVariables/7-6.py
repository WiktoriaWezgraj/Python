'''6. The speed of vehicles on a highway in Poland must be between 40 and 140 km/h. Write a program that checks whether the vehicle speed entered from the keyboard is correct.
Sample result:

    Enter vehicle speed: 158
    Speed is valid: False'''

speed = float(input('Enter vehicle speed: '))
speed_val = 40 <= speed <= 140
print(f'Speed is valid: {speed_val}')