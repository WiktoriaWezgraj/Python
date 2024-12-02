'''1. An array contains values: 2, 3, 7, 5, 4. Write a program that prints:
   1. the array
   1. number of elements
   1. first value
   1. second value
   1. last value
   1. last but one value (do not use negative index values)
   1. sum of the first and last value
   1. middle value
   1. all array values separated by a single space (use a loop statement)

   ###
   # Prints some array elements
   #'''
arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print(arr[-1])
print(arr[len(arr)-1])
print(arr[0]+arr[-1])
print(arr[len(arr)//2])
for i in arr:
   print(i, end=" ")