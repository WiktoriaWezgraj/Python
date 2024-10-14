'''2. Write a program, a temperature converter, that reads temperature in degrees Celsius from the keyboard. 
Then, the program calculates and prints the temperature in Kelvin and Fahrenheit.'''

    ###
    # A program that reads temperature in degrees Celsius from the keyboard.
    # Use comments to briefly describe the program's algorithm.
    #

temperature = float(input("Enter temperature in Celcius: "))
print("Kelvin: ", temperature+273.15, "Farenheit: ", (temperature*9/5) +32 )