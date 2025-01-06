''' Create a function f(n) that returns the difference between the largest and smallest odd digit contained in the number n. 
When the number n does not contain odd digits, the function returns -1. Example:а 

f(10852) à 4 
f(723597) 3à 6 
f(4388) à 0 
f(846206) à -1'''

def f(n):
    odd = []
    for i in str(n):
        if int(i)%2 == 1:
            odd.append(i)
    if odd == []:
        return -1
    diff = int(max(odd)) - int(min(odd))
    return diff

print(f(10852))
print(f(846206))
