'''Write a program that counts the number of occurrences of any value from a tuple. Sample result:

Tuple: 50,20,40,50,30,50
Value: 50
Number of occurrences: 3'''

def occurency(tuple,value):
    count = 0
    for i in tuple:
        if i==value:
            count += 1
    return count

print(occurency((50,20,40,50,30,50), 50))