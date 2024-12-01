'''An array contains integer numbers: 2, 6, 4, 9, 7. Create a program that prints the array values graphically as below. 
Define a function star(n) that returns the given number of asterisks as a string. Use a defined function in the program.

2: **
6: ******
4: ****
9: *********
7: *******'''

arr = [2, 6, 4, 9, 7]
def star(n):
    return '*' * n

for i in arr:
    print(f"{i}: {star(i)}")
