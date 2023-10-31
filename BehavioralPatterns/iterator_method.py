from abc import ABC, abstractmethod


class Book:
    def __init__(self, title, author, book_type):
        self.title = title
        self.author = author
        self.book_type = book_type


class Iterator(ABC):
    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def has_next(self):
        pass


class BookIterator(Iterator):
    def __init__(self, books):
        self.books = books
        self.current_book = 0

    def next(self):
        if self.current_book < len(self.books):
            current_book = self.books[self.current_book]
            self.current_book += 1
            return current_book
        else:
            return None

    def has_next(self):
        return self.current_book < len(self.books)


class IterableCollection(ABC):
    @abstractmethod
    def get_iterator(self):
        pass

    @staticmethod
    def display(iterator):
        while iterator.has_next():
            book = iterator.next()
            print(f'Book: {book.title}, Author: {book.author}, Type: {book.book_type}')
        else:
            print('')


class Library(IterableCollection):
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def get_iterator(self):
        return BookIterator(self.books)

    def filter_by_type(self, book_type):
        return BookIterator([book for book in self.books if book.book_type == book_type])

    def filter_by_name(self, book_name):
        return BookIterator([book for book in self.books if book.title == book_name])

    def filter_by_author(self, author):
        return BookIterator([book for book in self.books if book.author == author])


if __name__ == '__main__':

    library = Library()

    book1 = Book("War and Peace", "Leo Tolstoy", "novel")
    book2 = Book("Crime and Punishment", "Fyodor Dostoevsky", "novel")
    book3 = Book("The Catcher in the Rye", "J.D. Salinger", "novel")
    book4 = Book("The Hobbit", "J.R.R. Tolkien", "fantasy")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)

    book_iterator = library.get_iterator()
    library.display(book_iterator)

    novels = library.filter_by_type("novel")
    library.display(novels)

    fantasies = library.filter_by_type("fantasy")
    library.display(fantasies)
