'''Write a program that counts how many times each word appears in a paragraph.

Hint: Check the dictionary to see if the next word appears in it. 
If so, increase the number of times the word appears by 1. You can easily split a paragraph into individual words using the split() method. 
Search the Internet for how to use it.
'''
paragraph = "cat dog mouse cat rat cat mouse" #cat-3 dog-1 mouse-2 rat-1
arr = paragraph.split()

dictionar = {}

for word in arr:
    if word in dictionar:
        dictionar[word] += 1
    else:
        dictionar[word] = 1

        
print(dictionar)