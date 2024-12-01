'''Create a program that sorts elements of an array containing integer numbers. Apply the Bubble Sort sorting algorithm. 
Define a function bubblesort(array) that returns the sorted array. Try to sort and print any three arrays.'''
# procedure bubbleSort(arr):
#     n = length(arr)
#     for i = 0 to n-1:
#         for j = 0 to n-i-2:
#             if arr[j] > arr[j+1]:
#                 swap arr[j] and arr[j+1]
#       return arr

def bubblesort(array): ##wazne
    n = len(array)
    for i in range(n):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

print(bubblesort([7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]))
print(bubblesort([-150, -20, 300, -45, -60, 500, -120]))