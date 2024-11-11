'''28. A natural number greater than 1 is called a prime if it has exactly 2 natural factors with the values 1 and this number. 
Write a program that finds N leading prime numbers. Read the value of N from the keyboard. 
Using loop statements check that the number N is divisible only by 1 and by N.

    Prime numbers: 2 3 5 7 11 ...'''


N = int(input("Enter the number of prime numbers you want to find: "))

count = 0  
num = 2    

while count < N:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            pass
    if is_prime:
        print(num, end=" ")
        count += 1
    num += 1  


