class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def set_information(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def display_information(self):
        print("Title: ", self.title, '   \t', "Author: ", self.author, '   \t', "Genre: ", self.genre)
        
# Create an instance of the class - Book.
my_book = Book(title="Naruto", author="Masashi Kishimoto", genre="Shounen")
my_book.display_information() #Displays info.

# Updates new information using the set_information method which was defined earlier.
my_book.set_information(title="One Piece", author="Eiichiro Oda", genre="Shounen")
my_book.display_information() #Displays the Updated Information.
