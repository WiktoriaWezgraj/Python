'''4. Write a program that acts as a simple calculator. The program asks the user to enter a symbol of 
mathematical operation (+, -, *, /) and two numbers. Then, the program performs the appropriate mathematical 
operation on the given numbers and returns the result. Using the program, calculate:

    * 2 + 3
    * 2 * 4
    * 3 - 5
    * 5 * 6'''

    ###
    # Simple calculator
    # Asks the user to enter a symbol of mathematical operation (+, -, *, /)
    # and two numbers. The program should perform the appropriate
    # mathematical operation on the given numbers and return the result.   
    # 
number1 = int(input('Enter a number: '))
number2 = int(input('Enter a number: '))
operator = input('Enter an operator: ')

if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator == '/':
    result = number1 / number2
else:
    result = number1 * number2

    # print result
print(f'{number1} {operator} {number2} = {result}')
