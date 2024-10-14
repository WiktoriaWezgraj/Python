'''3. Write a program that calculates the volume and surface area of ​​a cuboid with sides a, b, and c. Then, check the program for the following data:

    a = 3, b = 4, c = 5 --> volume = 94, surface area = 60
    a = 8, b = 1, c = 2 --> volume = 16, surface area = 52'''

    ###
    # A program that calculates the volume
    # and surface area of ​​a cuboid with sides a, b, and c.
    # Read the dimensions of the cuboid from the keyboard.
    #
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
area = a * b * c
volume = a * b * 2 + a * c * 2 + b * c * 2
print(f"Volume is {volume}. Area is {area}")
