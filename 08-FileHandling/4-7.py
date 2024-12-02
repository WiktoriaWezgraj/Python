'''Write a program that calculates the number of vowels in the text entered from the keyboard. Use regular expressions.'''

import re

input_text = input('Enter the text: ')
# vowels = ['e', 'u', 'i', 'o', 'a']
pattern = '([euioa])'
amount = re.findall(pattern, input_text)

print(len(amount))
