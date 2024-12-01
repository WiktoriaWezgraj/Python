'''A two-dimensional array of size 2 by 4 contains integer numbers. Create a program that prints array values in rows and columns.'''
arr = [[1,2, 2,3], [4,5, 6,7]]

for row in arr:
    for i in row:
        print(i, end = " ")
    print()