'''27. The sequence of digits contains the number of points rolled with a dice. Define a function f(dice) that returns a number specifying the number of dice rolled the most times in a row. Sample result:

    f("5233165554211") returns 5
    f("2133") returns 3'''

def f(dice):
    max_digit = ""
    max_count = 0
    current_digit = ""
    current_count = 0
    
    for char in dice:
        if char == current_digit:
            current_count += 1
        else:
            current_digit = char
            current_count = 1

        if current_count > max_count:
            max_count = current_count
            max_digit = current_digit

    return int(max_digit)
    

print(f("2133"))