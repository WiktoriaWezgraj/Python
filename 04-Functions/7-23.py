'''23. An expression contains operators for adding and subtracting single-digit numbers.
 Define a function f(expression) that returns the value of the expression. Sample result:

    ```
    f("2+3") returns 5
    f("3+8+1") returns 12
    f("2+3-4+5-0") returns 6'''

def f(expression):
    result = 0
    sign = 1
    current_num = 0
    # return eval(expression)
    for char in expression:
        if char.isdigit():
            current_num =int(char)
            result += sign * current_num
        elif char == '-':
            sign = -1
        elif char == '+':
            sign = 1
    return result

print(f("2+2-1"))

