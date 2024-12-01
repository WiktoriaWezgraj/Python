'''A two-dimensional array of the size 3 by 5 contains integer numbers. 
Create a program that swaps the first and the last row. Print array values in rows and columns before and after changes.'''

arr = [
    [1,2,3,4,5],
    [2,3,4,5,6],
    [3,4,5,6,7]
]

arr[0], arr[-1] = arr[-1], arr[0]
print(arr)