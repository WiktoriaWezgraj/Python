'''An array contains values: 15, 8, 31, 47, 2, 19. 
Create a program that calculates and prints the array and the arithmetic mean of array values. Use the “while” loop statement.'''

arr = [15, 8, 31, 47, 2, 19]
counter = 0
sum = 0
while counter<len(arr):
    sum += arr[counter]
    counter += 1

mean = sum/len(arr)

print(mean)