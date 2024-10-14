'''8. Write a program that prints results of three dice rolls and the sum of dice rolled. Apply a random number generator.'''

    ###
    # A program that prints results of three dice rolls
    # and the sum of dice rolled.
    #
import random
dice_roll_1 = random.randint(1,6)
dice_roll_2 = random.randint(1,6)
dice_roll_3 = random.randint(1,6)
    
total = dice_roll_1 + dice_roll_2 + dice_roll_3
print(f"Dice 1: {dice_roll_1}. Dice 2: {dice_roll_2}. Dice 3: {dice_roll_3}. Total: {total}")