'''An array contains integer numbers:

[[-38, 19], [5,40],[-7,11],[29,16]]
Create a program that finds the smallest and largest values in the array and in which row and column they are located.'''

arr = [[-38, 19], [5,40],[-7,11],[29,16]]
largest = arr[0][0]
smallest = arr[0][0]
largest_position = (0, 0)
smallest_position = (0, 0)
for row_i, row in enumerate(arr):
    for column_i, column in enumerate(row):
        if column> largest:
            largest = column
            largest_position = (row_i, column_i)
        elif column< smallest:
            smallest = column
            smallest_position = (row_i, column_i)
print(largest, largest_position, smallest, smallest_position)
