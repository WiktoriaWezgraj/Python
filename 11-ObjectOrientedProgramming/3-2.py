'''Create a class that represents pieces of music. 
Define a class constructor that allows you to set the initial values of the music piece (artist, track title, album, year) when the object is created.
Complete the class with the __str__ method returning the song data as a string, in the format as below (4 lines). 
Then, create two objects that represent two pieces of music and print their data. Sample result:'''

class Music():
    def __init__(self, artist, title, album, year):
        self.artist = artist
        self.title = title
        self.album = album
        self.year = year

    def __str__(self):
        return f"{self.artist}\n {self.title}\n {self.album}\n {self.year}/n"
    
music = Music('Ed Sheeran', 'Hearts Dont Break Around Here', 'Divide', 2017)
print(music)