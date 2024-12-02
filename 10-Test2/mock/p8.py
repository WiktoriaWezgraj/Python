'''(p8.py) Reverse Polish Notation (RPN) is a mathematical notation in which operators follow their operands, e.g. 2 3 + 4 *. Define a function f(expression) that, for an RPN expression, returns the value of that expression. The expression contains only non-negative integers and the + and - operators. Example: 

f("2 3 +") à 5 
f("2 6 + 4 5 - +") à 7 
f("11 7 + 15 - 14 +") à 17'''

def f(expression):
    stack = []  # Initialize an empty stack
    tokens = expression.split()  # Split the RPN expression into tokens
    
    for token in tokens:
        if token.isdigit():  # If the token is a number
            stack.append(int(token))  # Push it onto the stack
        elif token in '+-':  # If the token is an operator
            # Pop the last two numbers from the stack
            b = stack.pop()
            a = stack.pop()
            
            # Perform the operation and push the result
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
        else:
            raise ValueError(f"Invalid token: {token}")
    
    # At the end, the stack should have only one element: the result
    return stack[0]

print(f("2 3 +"))