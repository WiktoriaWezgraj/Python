''' Create a function f(word) that, for a given word, 
returns a string of characters in which the subsequent 
letters of the word form the so-called Mexican Wave. 
Initially, the first letter of the word is capitalized
and the remaining letters are lowercase. Then, the second 
letter of the word is capitalized and the remaining letters 
are lowercase, etc. Separate words with a minus sign. Example: 

f("book") - "Book-bOok-boOk-booK" 
f("water") - "Water-wAter-waTer-watEr-wateR" 
f("ok") - "Ok-oK" 
f("a") - "A" 
f("") - "" '''

def f(word):
    arr = []
    for i in range(len(word)):
        wave = word[:i] + word[i].upper() + word[i+1:].lower()
        arr.append(wave) 
    return '-'.join(arr)

print(f("book"))


