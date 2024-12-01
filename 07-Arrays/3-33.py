'''A two-dimensional array of the size 3 by 5 contains integer numbers. 
Create a program that swaps the first and the last column. Print array values in rows and columns before and after changes.'''

arr = [
    [1,2,3,4,5],
    [2,3,4,5,6],
    [3,4,5,6,7]
]

for row in range(len(arr)):
    arr[row][0], arr[row][-1] = arr[row][-1], arr[row][0]

print(arr)