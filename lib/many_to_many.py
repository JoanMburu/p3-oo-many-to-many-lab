class Author:
    all = []

    def __init__(self, name):
        self.name = name
        self._contracts = []
        Author.all.append(self)

    def contracts(self):
        return self._contracts

    def books(self):
        return [contract.book for contract in self._contracts]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("book must be an instance of the Book class.")
        contract = Contract(self, book, date, royalties)
        self._contracts.append(contract)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._contracts)


class Book:
    all = []

    def __init__(self, title):
        self.title = title
        self._contracts = []
        Book.all.append(self)

    def contracts(self):
        return self._contracts

    def authors(self):
        return [contract.author for contract in self._contracts]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
        self.author._contracts.append(self)  # Add contract to author's list of contracts
        self.book._contracts.append(self)    # Add contract to book's list of contracts

    @property
    def author(self):
        return self._author

    @property
    def book(self):
        return self._book

    @property
    def date(self):
        return self._date

    @property
    def royalties(self):
        return self._royalties

    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of the Author class.")
        self._author = author

    @book.setter
    def book(self, book):
        if not isinstance(book, Book):
            raise Exception("book must be an instance of the Book class.")
        self._book = book

    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise Exception("date must be a string.")
        self._date = date

    @royalties.setter
    def royalties(self, royalties):
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer.")
        self._royalties = royalties

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]