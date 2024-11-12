'''11. Very often, there is a need to organize the data contained in the array. Organized data allows for faster retrieval, analysis, 
and presentation of information. There are many sorting algorithms that organize data in the array. One of the simplest is bubble sort, 
which organizes data in ascending or descending order. Bubble Sort is one of the simplest sorting algorithms. It works by repeatedly stepping through the 
list or array, comparing adjacent elements, and swapping them if they are in the wrong order. This process is repeated until no more swaps are needed, which 
means the list is sorted. Here is the bubble sort algorithm expressed in pseudocode, a universal notation that is independent of the programming language:

procedure bubbleSort(arr):
    n = length(arr)
    for i = 0 to n-1:
        for j = 0 to n-i-2:
            if arr[j] > arr[j+1]:
                swap arr[j] and arr[j+1]
      return arr'''

# 11. Define a function that sorts an array of numbers using the bubble sort algorithm. Use the information in the pseudocode provided earlier. Then, write a program that sorts the following collections of data:
   ###
   # Bubble sort
   #
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
print(car_fuel_consumption)
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption) 
print(sorted_car_fuel_consumption)

bank_transactions = [-150, -20, 300, -45, -60, 500, -120]
print(bank_transactions)
sorted_bank = bubble_sort(bank_transactions) 
print(sorted_bank)
