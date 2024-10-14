'''9. In many games, the numbers one and six on dice have special meaning. 
Write a program that prints the number of dice rolled and the value True if the number rolled is 1 or 6. Sample result:

    Dice rolled: 4
    Special number (1 or 6): False'''

import random
dice_1 = random.randint(1,6)
special_number = dice_1 == 1 or dice_1 == 6

print(f"Dice rolled: {dice_1}. Special number: {special_number}")
