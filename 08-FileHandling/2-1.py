'''1. Here's a program that writes data containing the title of a movie, its director, and the lead actor to a text file. 
Copy the program to the movie.py file, then run the program. Finally, open the created text file in an editor and check its contents.

   > To write data to a file, you need to open it with the 'w' (write) parameter. The write() method writes one line of data to the file. 
Note the '\n' character. It means to move the cursor to the next line. If you don't add it, all subsequent data will be placed on one line.
'''
   # Program to write movie details to a text file

   # Variables containing movie details
movie_title = "Inception"
director = "Christopher Nolan"
lead_actor = "Leonardo DiCaprio"

   # Name of the file to write to
file_name = 'movie_details.txt'

   # Writing movie details to the file
with open(file_name, 'w') as file:
    file.write(f"Movie Title: {movie_title}\n")
    file.write(f"Director: {director}\n")
    file.write(f"Lead Actor: {lead_actor}\n")

print(f"Movie details have been written to {file_name}.")

'''   Read the explanation of the program:

   * Variables: movie_title, director, and lead_actor hold the details of the movie.
   * Opening the file: with open(file_name, 'w') opens the file in write mode ('w'), creating or overwriting the file.
   * Writing details: Uses the write() method to write each movie detail to the file, adding \n at the end of each line for formatting (move to next line).
   * Automatic file closing: The 'with' statement ensures the file is properly closed after writing.'''