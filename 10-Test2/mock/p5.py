'''(p5.py) Define a function f(first_letter,last_letter) that, for the data.txt file, 
returns the number of words that start with the first_letter and end with the last_letter. Example: 

f("w","d")'''

import re

def f(first_letter, last_letter):
    with open('data.txt') as file:
        content = file.read()

    pattern = f'^{first_letter}[a-z]*{last_letter}$'

    total= 0
    splitted = content.split()
    for word in splitted:
        matched = re.match(pattern, word)
        if matched:
            total += 1

    return total

print(f('w', 'd'))
