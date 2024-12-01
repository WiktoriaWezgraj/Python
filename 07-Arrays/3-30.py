'''An array contains values:

[[0,0,0,0,0],0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] 
Create a program that modifies the array values to create a multiplication table as below. Use loop statements. Print the array.

1  2  3  4  5
2  4  6  8 10
3  6  9 12 15
4  8 12 16 20
5 10 15 20 25'''

arr = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] 
for i in range(0, len(arr[0])):
    arr[0][i] = i+1

for i in range(0, len(arr[1])):
    arr[1][0] = arr[0][1]
    arr[1][i] = arr[1][0] * arr[0][i]

for i in range(0, len(arr[2])):
    arr[2][0] = arr[0][2]
    arr[2][i] = arr[2][0] * arr[0][i]

for i in range(0, len(arr[3])):
    arr[3][0] = arr[0][3]
    arr[3][i] = arr[3][0] * arr[0][i]

for i in range(0, len(arr[4])):
    arr[4][0] = arr[0][4]
    arr[4][i] = arr[4][0] * arr[0][i]

print(arr)

