'''The reduce() function in Python, which is available in the functools module, is used to apply a function cumulatively to the elements of an iterable, 
reducing it to a single value. Syntax:

from functools import reduce

reduce(function, iterable[, initializer])
Where:

function: A function that takes two arguments and performs an operation on them.
iterable: The iterable (like a list, tuple, etc.) whose elements are reduced.
initializer (optional): An initial value to start the reduction process.
How reduce() works:

Takes a function that accepts two arguments.
Applies the function to the first two elements of the iterable.
Uses the result of the function to combine with the next element.
Repeats this process until all elements have been processed.
Returns a single, reduced value as the final result.
The following program calculates the sum of numbers. 
Notice the use of the reduce() function. Then modify the program: replace the regular function add(x,y) with an anonymous function.

from functools import reduce

# Function to add two numbers
def add(x, y):
   return x + y

numbers = [1, 2, 3, 4, 5]

# Using reduce to sum the numbers
result = reduce(add, numbers)
print(result)  # Output: 15'''

from functools import reduce

def add(x, y):
   return x + y

numbers = [1, 2, 3, 4, 5]

result = reduce(add, numbers)
print(result)