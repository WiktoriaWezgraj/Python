'''1. The vowels.py program counts vowels in the text. Modify the program. Replace the 'for' statement with a 'while' statement. '''
###
# Counts vowels in the text
#
text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0
i = 0

while i < len(text):
    if text[i] in vowels:
        vowel_count += 1
    i += 1
# Count vowels in the text
'''for char in text:
    if char in vowels:
        vowel_count += 1'''

print(f"The number of vowels in the text is: {vowel_count}")
