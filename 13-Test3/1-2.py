''' Create a function f(x,y,digit) that returns how many 
times the given digit appears in numbers in the range from x to y. 
Example: 

f(10,15,1) - 7 
f(28,32,2) - 3 
f(100,105,6) - 0 
f(100,101,0) - 3 '''

def f(x,y,digit):
    count = 0
    for i in range(x,y+1):
        for num in str(i):
            if num == str(digit):
                count += 1
    return count

print(f(10,15,1))
print(f(28,32,2))