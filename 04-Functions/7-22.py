'''22. A valid password should consist of at least six characters and each character appears only once in the password. 
Define a function f(password) that returns True if the password is correct or False otherwise. Sample result:

    f("ax15") returns False
    f("book123") returns False
    f("A2water3") returns True
    f("qwerty") returns True
    f("") returns False'''

def f(password):
    is_valid = False
    if len(password) >= 6:
        if len(set(password)) == len(password):
            is_valid = True
    return is_valid

