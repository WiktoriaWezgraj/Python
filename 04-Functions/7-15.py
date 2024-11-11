'''15. Define the function f(n), which returns the n-th value of the Fibonacci sequence. 
The sequence is defined as follows: the first value of the sequence is 0, the second value is 1. 
Each subsequent value is the sum of the previous two. Sample result:

    f(5) returns 3
    f(9) returns 21'''

def f(n):
    a = 0
    b = 1
    if n == 1:
        return a
    if n == 2:
        return b
    for i in range(3,n+1):
        a, b = b,a+b
    return b
        
print(f(9))
