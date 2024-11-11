'''25. Define a function f(text) that returns the given text with all characters separated by \"-\" (minus sign). Example:

    f("University") returns "U-n-i-v-e-r-s-i-t-y"
    f("UE") returns "U-E"
    f("x") returns "x"
    f("") returns ""'''

def f(text):
    return "-".join(text)
