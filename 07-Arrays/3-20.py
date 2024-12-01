'''Write a program to separate even and odd numbers of a given array of integers. Put all even numbers first, and then odd numbers.

Sample result:

arr = [7,9,2,4,5,6]
...
...
arr = [2,4,6,7,9,5]'''

even = []
odd = []
arr= [7,9,2,4,5,6]
for num in arr:
    if num%2 ==0:
        even.append(num)
    if num%2 ==1:
        odd.append(num)

arr = even + odd
print(arr)