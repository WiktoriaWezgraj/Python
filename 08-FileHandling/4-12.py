'''The file books.csv contains a list of books. 
Write a program that copies the book data from a given genre to its corresponding file. 
Use functions to divide the program into logical parts.

Genre --> Filename
Fantasy --> books_fantasy.txt
Historical --> books_historical.txt
Romance --> books_romance.txt
Classic --> books_classic.txt  '''

import csv

genre_files = {
    "Fantasy": "books_fantasy.txt",
    "Historical": "books_historical.txt",
    "Romance": "books_romance.txt",
    "Classic": "books_classic.txt"
}

with open('books.csv') as file:
    csvreader = csv.DictReader(file)

    for row in csvreader:
        genre = row["Genre"]
        if genre in genre_files:
            book_info = f"{row['Title']}, {row['Author']}, {row['Year']}"
            with open(genre_files[genre], 'a') as f:
                f.write(book_info + '\n')
