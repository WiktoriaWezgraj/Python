'''8. Create a function f(number, even) that computes the sum of the digits of a number. When the value of the even parameter is True, 
the function returns the sum of the even digits. When the value of the even parameter is False, the function returns the sum of the odd digits. Sample result:

    f(3124,True) returns 6
    f(3124,False) returns 4
    f(20576,False) returns 12
    f(20576,True) returns 8
    f(13115,True) returns 0'''

def f(number, even):
    even_sum = 0
    odd_sum = 0
    number = str(number)
    for num in number:
        num = int(num)
        if num%2 == 0:
            even_sum += num
        if num%2 == 1:
            odd_sum += num
    if even == True:
        return even_sum
    return odd_sum
    
