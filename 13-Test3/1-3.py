'''The uid array contains user IDs in one of the popular websites. 
Identifiers should be unique. Create a function f(uid) that 
returns true if all ids are unique. Otherwise, the function 
returns false. Example: 

f(["john5","ann123","JOHN5","xxx","abc333","a10"]) à True 
f(["abc123","ann","abc123","a10"]) à False 
f(["bob2","bob2"]) à False 
f(["bob2","BOB2"]) à True '''

def f(uid):
    return len(uid) == len(set(uid))

print(f(["bob2","bob2"]))
