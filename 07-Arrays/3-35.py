'''Create a function transpose_matrix(m) that returns transposed matrix m:

https://en.wikipedia.org/wiki/Transpose

Then, create a program that prints transposed matrices, in rows and columns, for the following matrices.

1 2 3
4 5 6
7 8 9
1 2 3 4 5
6 7 8 9 0
5 6 7 8'''

def transpose_matrix(m):
    # Get the number of rows and columns
    rows = len(m)
    cols = len(m[0])

    # Initialize an empty matrix for the transposed matrix
    transposed = [[0] * rows for _ in range(cols)]

    # Populate the transposed matrix
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = m[i][j]

    return transposed
    