'''An array contains numbers from 1 to 20. Write a program that calculates and displays their third power. Use the map() and an anonymous function.'''

arr = [i for i in range(1,21)]
result=list(map(lambda num: num**3, arr))
print(result)