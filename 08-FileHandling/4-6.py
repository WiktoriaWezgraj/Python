'''Write a program that calculates the number of lines, characters and words for any text file. 
The user enters the name of the file from the keyboard. Use a try-except block to avoid 
interrupting your program when the user enters a filename that doesn't exist. 
Print the result of the calculation. To check if the program is working correctly, 
find 3 text files on the Internet and use them to test the program.Sample result:

File name: books.csv <- this exists
Number of lines: 14
Number of characters: 2540
Number of words: 703'''

file_name = 'books.csv'
sum_lines = 0
sum_char = 0
sum_words = 0
try:
    with open(file_name) as f:
        for line in f:
            sum_lines += 1
            sum_char += len(line)
            sum_words += len(line.split()) ##wazne
except FileNotFoundError:
    print('File not found.')
print(sum_char)
print(sum_lines) ## how to deal with csv and json
print(sum_words)