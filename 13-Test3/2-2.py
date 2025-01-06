'''Create a function f(x,y,d) that returns true when the string of digits d appears in any number between x and y. Otherwise, the function returns false.  Example: 

f(10,15,"14") à True 
f(100,120,"11") à True 
f(205,210,"04") à False '''

def f(x,y,d):
    for i in range(x,y):
        if d in str(i):
            return True
    return False

print(f(10,15,"14"))
print(f(100,120,"11"))
print(f(205,210,"04"))

