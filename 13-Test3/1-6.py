'''Assume that a valid variable name in a computer program consists of one to five characters. 
The first character of a variable name must be a lowercase or uppercase letter or an underscore. 
The remaining characters in the variable name can be uppercase or lowercase letters, digits or the underscore character. 
Create a function f(vname) that returns true if the variable name vname is valid. Otherwise, the function returns false. Example: 

f("abc") à True 
f("Abc") à True 
f("aBC") à True 
f("_ab_c") à True 
f("abcdef") à False 
f("8abc") à False 
f("_aB8_") à True 
f("_4x") à True '''

import re
def f(vname):
    pattern = r"^[A-Za-z_][A-Za-z_1-9]{0,5}$"
    if re.match(pattern, vname):
        return True
    else:
        return False
    
print(f("abc"))
print(f("8abc"))