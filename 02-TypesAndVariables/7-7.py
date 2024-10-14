'''7. Each programming language provides a set of functions that you can use in your programs. 
One of them is a function randint(a,b) that returns a integer random number in the range <a,b>. 
The function is available in a module called random, which you need to import into your program.

    <https://docs.python.org/3/library/random.html>

    Analyze the program below. Then, run the program five times and see what numbers are generated.'''

import random
random_number = random.randint(5,10)
print(random_number)