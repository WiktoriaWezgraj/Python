'''3. The file pets.txt contains humorous text about animals. Write a program that prints the text and counts the number of words in the text.

   > To calculate the number of words in a line, use the split() method, which splits a string into a list where each word is a list item.
     Then read the length of this list. Use the len() function. Finally, sum the number of words in each line.\
   <https://www.w3schools.com/python/ref_string_split.asp>'''

with open("pets.txt") as f:
  content = f.read()

len_of_words = len(content.split())
print("wORD COUNT:", len_of_words)
