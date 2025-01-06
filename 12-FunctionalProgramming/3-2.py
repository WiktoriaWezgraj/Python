'''For the following text:

I completely agree with you
write a program that calculates and displays the number of letters in each word. Use the map() and an anonymous functions to calculate the number of letters.

Tip: to split text into words, use the split() function.

Sample result:

Text: I completely agree with you
No. of letters in words: [1,10,5,4,3]
sentence = '...'
result = list(map(lambda ... , sentence. ...))
print(result)'''

sentence = 'I agree with you'
result = list(map(lambda word: len(word), sentence.split()))
print(result)