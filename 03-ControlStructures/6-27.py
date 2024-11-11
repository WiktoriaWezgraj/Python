'''27. Write a program that prints the first twenty words of the Fibonacci sequence. 
The sequence is defined as follows: the first term is equal to 0, the second is equal to 1, each subsequent term is the sum of the previous two. 
Sample result:

    <https://en.wikipedia.org/wiki/Fibonacci_number>

    0 1 1 2 3 5 8 13 21 34 ...'''

number = 0
number_2 = 1
print(number, number_2, end=" ")
for i in range(1,19):
    next_number = number + number_2
    print(next_number, end = " ")
    number, number_2 = number_2, next_number
