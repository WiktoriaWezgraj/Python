'''An array contains a list of Polish names:

Genowefa, Onufry, Celestyna, Alojzy, Pankracy
Create a program that prints the longest name (consisting of the largest number of characters). Sample result:

Names: Genowefa Onufry Celestyna Alojzy Pankracy
Longest name: Celestyna'''

arr = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
longest = arr[0]
for i in arr:
    if len(i) >len(longest):
        longest = i

print(longest)
