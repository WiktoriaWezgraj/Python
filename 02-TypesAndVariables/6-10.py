'''10. Every programming language has a number of ready-to-use functions that you can use to manipulate strings. 
The most commonly used ones in Python can be found at:

    <https://www.w3schools.com/python/python_ref_string.asp>'''


    ###
    # String manipulation
    #

movie = "The Lord of the Rings: The Return of the King"

    # print number of characters
print('Number of characters: ', len(movie))

    # print title in capital letters
print(movie.upper())

    # print title in small letters
print(movie.lower())

    # print how many times the vowel "e" appears in the title
print(movie.lower().count("e"))

    # print where in the text is the word "Lord"
print(movie.index("Lord"))

    # print where in the text is the word "dragon"
word = "dragon"
print(word.lower().find(word.lower()))