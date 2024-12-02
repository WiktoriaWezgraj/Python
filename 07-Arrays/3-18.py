'''Create a module MyArrays containing functions to operate on an array of numbers:

-A function that returns the second largest element in an array
-A function that returns the difference between the largest and smallest values in an array
-A function that returns the median of numbers in an array.
Do not use built-in functions. The median is the middle value in the ordered sequence of numbers:

https://en.wikipedia.org/wiki/Median#/media/File:Finding_the_median.png

-A function that returns a two-element array containing the smallest and largest values in an array

-A function that returns array elements as a string, separated by the minus sign

Then, write a program that for the sequence of numbers:

7,3,8,5,2
calculates and prints results. Sample result:

Numbers: 7,3,8,5,2
Second largest number: 7 
Median: 5
Smallest and largest number: 2,8
Numbers as a string: 7-3-8-5-2'''

def MyArrays(arr):
    arr_sorted = sorted(arr, reverse=True)
    second_largest = arr_sorted[1]

    difference = arr_sorted[-1] - arr_sorted[0]

    median = 0
    if len(arr_sorted)%2==1:
        median_place = len(arr_sorted)//2 + 1
        median = arr_sorted[median_place-1]
    if len(arr_sorted)%2==0:
        median_place1 = len(arr_sorted)//2
        median_place2 = len(arr_sorted)//2 + 1
        median = arr_sorted[median_place1-1] + arr_sorted[median_place2-1] / 2

    arr2 = []
    arr2.append(arr_sorted[0])
    arr2.append(arr_sorted[-1])

    stri = ""
    for i in range(len(arr)):
        stri += str(arr[i])
        if i != len(arr)-1: 
            stri += "-"


    return second_largest, difference, median, arr2, stri



print(MyArrays([7,3,8,5,2]))
