'''19. Define the function f(n) that returns the n-th prime number. 
A prime number is a natural number greater than 1, divisible by 1 and that number. Sample result:

    f(1) returns 2
    f(5) returns 11'''

def f(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        is_prime = True
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return num

print(f(5))