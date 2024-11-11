'''4. In a separate module, define a function that checks if the number is within the range <x, y>. 
The function returns a boolean value. Then, create a program and use the function you defined. Sample result:


    A number: 7
    Number 7 in the range <2,15>: yes'''

def f(num, min_num, max_num):
    if num in range(min_num, max_num+1):
        return "yes"
    return "no"

print(f(7,2,15))