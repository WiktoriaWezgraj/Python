'''17. A sentence is an ordered group of words separated by spaces. Define a function f(sentence) that returns a sentence with spaces removed. Sample result:

    f("integrated development environment") returns
    "integrateddevelopmentenvironment"
    f("A programming language is a system of notation for writing
    computer programs") returns
    "Aprogramminglanguageisasystemofnotationforwritingcomputerprograms"'''

def f(sentence):
    result = ""
    for i in sentence:
        if i != " ":
            result += i
    return result

print(f("integrated development environment"))