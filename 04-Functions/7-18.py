'''18. Define a function f(number) that returns the sum of repeated digits in a number. Sample result:

    f(1027) returns 0
    f(230335) returns 9
    f(513553007) returns 21'''

def f(number):
    sum = 0
    strink = ""
    strink_repeated = ""
    for digit in str(number):
        if digit not in strink:
            strink+=digit
        elif digit in strink:
            strink_repeated += digit
    strink_repeated += strink_repeated[0]
    for num in strink_repeated:
        sum += int(num)
    return sum
        

print(f(230335))