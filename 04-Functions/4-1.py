'''1. Define a function **triangle_area** that calculates and returns the area of ​​a triangle with sides a, b, and c. Use Heron's formula:

    <https://en.wikipedia.org/wiki/Heron%27s_formula>

    Write a program that calculates the area of ​​a triangle based on the lengths of the triangle's sides read from the keyboard. Use the defined function. 
    Then calculate the area of ​​the triangle for the following dimensions of sides a, b, and c:

    * 3, 4, 5 (result is 6)
    * 5, 12, 13 (result is 30)
    * 7, 24, 25 (result is 84)'''

    ###
    # Calculates the area of a triangle based on the lengths
    # of the triangle's sides
    #
import math

def triangle_area(a,b,c):
    s = 1/2*(a+b+c)
    A = int(math.sqrt(s*(s-a)*(s-b)*(s-c)))
    return A

print(triangle_area(3,4,5))
