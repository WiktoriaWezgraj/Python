'''The following program calculates the sum of even numbers from 1 to a given number N using a for loop. 
Modify the program. Replace the 'for' statement with a 'while' statement.'''

    ###
    # Calculates the sum of even numbers from 1 to a given number N
    #
N = 10
sum_even = 0

    # Calculate the sum of even numbers
'''for i in range(1, N + 1):
    if i % 2 == 0:
        sum_even += i'''
i = 1
while i<=N:
    if i % 2 == 0:
        sum_even += i
    i += 1

print(f"The sum of even numbers from 1 to {N} is: {sum_even}")