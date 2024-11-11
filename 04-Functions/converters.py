'''1. The converters.py file defines two functions for converting length units (cm-->m and m-->cm). The test_converters.py file uses these functions to convert values.

    Define the following functions in the converters.py file that allow you to:

    * convert centimeters to inches
    * convert feet and inches to centimeters

    Then complete the main program to test the added functions.'''

def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_inch(n):
    inches = n * 0.393701
    return inches

def feet_inch_to_cm(feet,inches):
    total_cm = (feet * 30.48) + (inches * 2.54)
    return total_cm

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')

