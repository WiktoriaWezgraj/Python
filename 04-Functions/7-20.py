'''20. Define the function f(number1,number2,number3), which returns the difference between the largest and smallest numbers. Sample result:

    f(7,4,9) returns 5
    f(2,12,8) returns 10'''

def f(number1,number2,number3):
    smallest_num = number1
    if number2 < number1:
        smallest_num = number2
    elif number3 < number1:
        smallest_num = number3
    biggest_num = number1
    if number2 > number1:
        biggest_num = number2
    elif number3 > number1:
        biggest_num = number3
    return biggest_num - smallest_num

