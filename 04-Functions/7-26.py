'''26. Products are marked with a special code consisting of 3 digits and afourth control digit. 
The forth digit is determined by calculating the remainder of dividing the sum of the first three digits by 7. 
Define a function f(product_code) that returns True if the product code is correct or False otherwise. Sample result:

    f("1082") returns True
    f("2035") returns True
    f("1114") returns False
    f("7071") returns False'''

def f(product_code):
    sum = 0
    for i in product_code[0:3]:
        sum += int(i)
    last_digit = product_code[3]
    if sum%7 == int(last_digit):
        return True
    else:
        return False

print(f("2035"))