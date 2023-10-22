class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, authors: object):
        if isinstance(name, str) and isinstance(year, int):
            book = Book(name, year, authors)
            self.books.append(book)
            return book


    def group_by_author(self, author: object):
        return [item for item in self.books if item.author == author]

    def group_by_year(self, year: int):
        return [item for item in self.books if item.year == year]

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'

class Book:

    ALL_BOOKS = 0
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        Book.ALL_BOOKS += 1



    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}, {self.year}, {self.author}'



class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}, {self.country}, {self.birthday}'




library = Library("Library")
author = Author("Rowling", "UK", "31.07.1965")
author_2 = Author("Carroll", "UK", "27.01.1832")
author_3 = Author("G. Orwell", "UK", "25.06.1903")
book_1 = library.new_book("Alice in Wonderland", 1865, author_2)
book_2 = library.new_book("Harry Potter", 1997, author)
book_3 = library.new_book("1984", 1949, author_3)

print(library.group_by_author(author))
print(library.books)
print(library.group_by_year(year=1865))
print(Book.ALL_BOOKS)
