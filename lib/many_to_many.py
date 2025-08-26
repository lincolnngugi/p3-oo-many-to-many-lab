# lib/book_author_contract.py

class Book:
    all = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string.")
        self.title = title
        Book.all.append(self)

    def contracts(self):
        # Returns all contracts associated with this book
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        # Returns all authors associated with this book through contracts
        return [contract.author for contract in self.contracts()]


class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string.")
        self.name = name
        Author.all.append(self)

    def contracts(self):
        # Returns all contracts associated with this author
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        # Returns all books written by this author (via contracts)
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        # Creates a new contract between this author and the given book
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        # Sum of all royalties for this author
        return sum(contract.royalties for contract in self.contracts())


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        # Use property setters (they include validation)
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    # --- Author ---
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author must be an instance of Author.")
        self._author = value

    # --- Book ---
    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("book must be an instance of Book.")
        self._book = value

    # --- Date ---
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("date must be a string.")
        self._date = value

    # --- Royalties ---
    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("royalties must be an integer.")
        self._royalties = value

    # --- Class Method ---
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
