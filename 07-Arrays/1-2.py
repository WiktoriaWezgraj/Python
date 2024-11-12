'''2. An array contains values: 1, 2, 3, 4, 5. Write a program that modifies the array values. Print the array after each change.

   1. subtract one from the first element of the array
   1. increase the last array element by 4
   1. multiple the middle array element by 2

   Sample result:
   Array: [1,2,3,4,5]
   Array: [0,2,3,4,5]
   Array: [0,2,3,4,9]
   Array: [0,2,6,4,9]'''

arr = [1,2,3,4,5]
print(arr[0]-1)
print(arr[-1]+4)
print(arr[(len(arr)//2)]*2)
