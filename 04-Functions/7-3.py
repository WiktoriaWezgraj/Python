'''3. Write a program that calculates how many times the given letter appears in any text. 
Then create a program and check how many times the letter 'e' appears in the text below. 
In a separate module, define a function for making calculations. Sample result:

    You never get a second chance to make a first impression
    The number of letter 'e': 7'''

def f(letter, sentence):
    count = 0
    for i in sentence:
        i = str(i)
        if i.upper() == letter.upper():
            count += 1
    return count


