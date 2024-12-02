
'''(p10.py) A two-dimensional array contains different integer numbers. Define a function f(array) that returns True if the row and column numbers for the smallest value in the array are equal, and False otherwise. Example: 

f([[7,8],[5,3],[9,4]]) à True     # 3, row 1, col 1 
f([[7,8,5,3],[9,4,2,6]]) à False  # 2, row 1, col 2 '''

def f(array):
    smallest_value = array[0][0]
    smallest_position = [0,0]
    for row_index, row in enumerate(array):
        for col_index, value in enumerate(row):
            if value < smallest_value:
                smallest_value = value
                smallest_position = [row_index, col_index]

    return smallest_position[0] == smallest_position[1]

print(f([[7, 8], [5, 3], [9, 4]]))
                
