'''A variable contains text:

An apple a day keeps the doctor away

Create a module MyText, containing:

A function that returns the number of words in the text
A function that returns an ordered array of words, from longest to shortest
A function that returns an alphabetically ordered array of words
Then, write a program, call the functions and print results. Sample result:

Text: An apple a day keeps the doctor away
Number of words: 8
Words from the longest: doctor,apple,…
Words ordered alphabetically: a,An,apple,away,…'''

def num_of_words(var):
    var_arr = var.split()
    return len(var_arr)

def ordered_arr(var):
    var_arr = var.split()
    longest = sorted(var_arr, key=len, reverse= True) ##wazne
    return longest

def alphabetic_ord(var):
    var_arr = var.split()
    alph = sorted(var_arr)
    return alph

print(num_of_words("An apple a day keeps the doctor away"))
print(ordered_arr("An apple a day keeps the doctor away"))
print(alphabetic_ord("An apple a day keeps the doctor away"))