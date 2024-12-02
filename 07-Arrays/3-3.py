'''An array contains integer numbers: 34,7,19,4,21,8. Create a program that calculates and prints the number of even values in the array. 
Use the ‘while’ loop statement.

An array contains natural numbers: 15, 8, 31, 47, 2, 19. Create a program that prints the contents of the array in reverse order. 
Use any loop statement. Sample result:

existed array: 15 8 31 47 2 19 
reverse array: 19 2 47 31 8 15
Create a program that computes the second power of each array element. Sample result:

Array: 8 2 5 1 9
2nd power: 64 4 25 1 81'''

def array_power3tasksinone(arr):
    count = 0
    sum = 0
    arr2 = []
    while count < len(arr):
        for i in arr:
            if i%2 == 0:
                count += 1
                sum += i
            else:
                count += 1

    arr_rev = arr[::-1]

    for y in arr:
        arr2.append(y**2)
    return arr2, arr_rev, sum

print(array_power3tasksinone([34,7,19,4,21,8]))