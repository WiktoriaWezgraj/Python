'''1. In addition to the built-in functions, you can use numerous functions available in ready-to-use modules. One example is the \'math\' module.

    <https://docs.python.org/3/library/math.html>

    Using functions and constants available in the \'math\' module, write a program that calculates and prints:

    * square root of 7
    * natural logarithm of 5
    * sine of 90 degrees'''


    ###
    # To use the functions available in an external module,
    # you must include that module in your program.
import math

square_root = math.sqrt(7)
print('A square root of 7 is', square_root)
natural_logarithm = math.log(5)
print(natural_logarithm)
sine = math.sin(90)    
print(sine)