'''Define a function that returns true if the brackets (), {}, [] are used correctly in the given expression. Otherwise, the function returns false. Then write a program that checks the correctness of the expressions given below.

Use a stack. Read the next characters of the expression. Skip all but the brackets. If it is an opening bracket, put it on the stack. If it is a closing bracket, get the item from the stack and compare whether it is a matching opening bracket.
'''
import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
    # Define matching pairs of brackets
    matching_brackets = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in expression:
        if char in "({[":
            # Push opening brackets onto the stack
            stack.append(char)
        elif char in ")}]":
            # If a closing bracket is found, check the stack
            if not stack or stack.pop() != matching_brackets[char]:
                return False  # Mismatched or unbalanced brackets

    # If stack is empty, all brackets were balanced
    return len(stack) == 0


# Expressions to check
expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"  # brackets ok
expression2 = "[(2+3]/4)"                  # brackets not correct
expression3 = "(2-3*4+(5/6)"               # brackets not correct

# Function to test expressions and print results
def test_expression(expression):
    if brackets_ok(expression):
        print(f"The brackets in '{expression}' are correct.")
    else:
        print(f"The brackets in '{expression}' are not correct.")


# Test expressions
test_expression(expression1)
test_expression(expression2)
test_expression(expression3)
