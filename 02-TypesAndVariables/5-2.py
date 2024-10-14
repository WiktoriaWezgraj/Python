'''2. Take into account that whatever the user types on the keyboard is captured as a string. If you need a number for some arithmetic calculations, 
you have to convert the string of digits from the keyboard to a number using the int() function for integer numbers and float() function for real numbers. 

    Complete the following program code. Then, check the program for the following data:

    a = 4 --> volume = 64, surface area = 96
    a = 7 --> volume = 343, surface area = 294'''

    ###
    # A program to calculate the volume and surface area of ​​a cube.
    # 
cube_side_string = input('Enter cube side: ')
cube_side = int(cube_side_string)
cube_volume = cube_side**3
cube_surface_area = cube_side**2*6
print(f'The volume of a cube with side {cube_side} is {cube_volume}')
print(f'The surface area of a cube with side {cube_side} is {cube_surface_area}')