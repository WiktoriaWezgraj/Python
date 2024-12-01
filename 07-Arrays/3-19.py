'''Write a program that, for the given array of real numbers, prints the number of elements 
that are greater than the given value entered from the keyboard.'''

def comparison(arr, value):
    for i in arr:
        if i> value:
            print(i)

comparison([2,3,4,5,6], 4)