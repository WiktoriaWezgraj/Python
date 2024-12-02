'''Create a function that convert two-dimensional (2D) array into 1D. Then create a program that prints 1D array for the following 2D arrays.

2 3
1 5
5 0 3 7 5
9 0 9 1 2
2 1
3 5
7 4
2 6'''

def transform(arr_2d):
    arr_1d = []
    for row in arr_2d:
        for i in row:
            arr_1d.append(i)
    return arr_1d

print(transform([[5, 0, 3, 7, 5],
[9, 0, 9, 1, 2]]))