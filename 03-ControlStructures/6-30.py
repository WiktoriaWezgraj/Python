'''30. Write a program that prints 20 integer random numbers in the range of 5 to 10.'''

import random
count = 0
while count < 20:
    print(random.randint(5,10), end= " ")
    count += 1