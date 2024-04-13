class Book:
    books_list = []

    def __init__(self, title, year_of_release, publisher, genre, author, price):
        self.title = title
        self.year_of_release = year_of_release
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price
        Book.books_list.append(self)

    @classmethod
    def input_data(cls):
        title = input("Enter book title: ")
        year_of_release = int(input("Enter year of release: "))
        publisher = input("Enter publisher: ")
        genre = input("Enter genre: ")
        author = input("Enter author: ")
        price = float(input("Enter price: "))
        return cls(title, year_of_release, publisher, genre, author, price)

    @classmethod
    def output_data(cls):
        print("Books:")
        for book in cls.books_list:
            print(f"Title: {book.title}, Year of release: {book.year_of_release}, Publisher: {book.publisher}, Genre: {book.genre}, Author: {book.author}, Price: {book.price}")

book1 = Book.input_data()
book2 = Book.input_data()

Book.output_data()