'''(p3.py) A two-dimensional array contains the same number of rows and columns. Define a function f(array2D) that, for the given two-dimensional array array2D, returns True when the sum of the values in each row of the array is equal to the sum of the values in the corresponding column (e.g., the sum of the values in row 3 is equal to the sum of the values in column 3) , and False otherwise. Example: 

f([[3,7,2],[4,2,5],[5,2,1]]) à True 
f([[3,7,2],[4,2,5],[9,2,1]]) à False '''

def f(array2D):
    n = len(array2D)
    for i in range(n):
        sum_row = 0
        sum_col = 0
        for j in range(n):
            sum_row += array2D[i][j]
            sum_col += array2D[j][i]

    if sum_row != sum_col:
        return False
    return True


print(f([[3,7,2], [4,2,5], [5,2,1]]))

# 3 7 2
# 4 2 5
# 5 2 1