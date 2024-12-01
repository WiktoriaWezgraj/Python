'''Define a function rand_elem(array) that returns a randomly selected array element. Using the function, print a few randomly selected array elements.'''
import random
def rand_elem(arr):
    return random.choice(arr)

print(rand_elem([1,2,3,4,5]))