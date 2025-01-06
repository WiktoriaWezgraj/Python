'''Write a program that calculates the sum of even numbers. Use filter(), reduce() and anonymous functions.

Tip. First, use filtering to extract even numbers. Then use reduce() to calculate the sum of those numbers.

numbers = [2,4,6,3,7,5]'''

from functools import reduce

numbers = [2,4,6,3,7,5]
even_num = list(filter(lambda x: x%2 == 0, numbers))
sum_of_even = reduce(lambda x,y: x+y, even_num)
print(sum_of_even)
