'''The following array represents a square matrix and contains values:

[
   [0,0,0],
   [0,0,0],
   [0,0,0]
]
Create a program that replaces the values of the main diagonal with 1. Use a loop statement. Print the modified array. Sample result:

1 0 0
0 1 0
0 0 1'''

matrix = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]

for row in matrix:
   for i in range(0 , len(row)):
      matrix[i][i] = 1
   for y in row:
      print(y, end=" ")
   print(" ")
