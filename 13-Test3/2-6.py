'''A valid number on the planet Metis consists of digits 1 to 7 and lowercase or uppercase letters a to d.
A plus (+) or minus (-) sign may also appear at the beginning of the number. The mnumbers array contains sample numbers. 
Create a function f(mnumbers) that returns how many numbers in the array that are valid in the planet Metis. Example: 

f(["A15","-31","7abC","+D1","-gH"]) à 5 
f(["A05","-3+1","7ab8C","+D1","-22k"]) à 1'''
import re

def f(numbers):
    count = 0
    pattern = r'^[+-]?[a-dA-D1-7]+$'
    for i in numbers:
        if re.match(pattern, i):
            count += 1
    return count

print(f(["A15","-31","7abC","+D1","-gH"]))
print(f(["A05","-3+1","7ab8C","+D1","-22k"]))