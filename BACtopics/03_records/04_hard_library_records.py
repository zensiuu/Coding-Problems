"""
RECORDS - HARD: Library Management
Hint: combine records + arrays + search

You manage a library. Each book is a dict with:
  - "id" (int), "title" (str), "author" (str), "year" (int)

Write three functions:
  1. add_book(library, book) — appends book to library list, returns it
  2. find_by_author(library, author) — returns list of books by that author
  3. books_before_year(library, year) — returns list of books published
     before the given year

Examples:
  lib = []
  add_book(lib, {"id":1,"title":"1984","author":"Orwell","year":1949})
  find_by_author(lib, "Orwell") -> [{"id":1,"title":"1984",...}]
"""

def add_book(library, book):
    pass

def find_by_author(library, author):
    pass

def books_before_year(library, year):
    pass


if __name__ == "__main__":
    lib = []
    add_book(lib, {"id": 1, "title": "1984", "author": "Orwell", "year": 1949})
    add_book(lib, {"id": 2, "title": "Brave New World", "author": "Huxley", "year": 1932})
    add_book(lib, {"id": 3, "title": "Animal Farm", "author": "Orwell", "year": 1945})
    assert len(lib) == 3
    assert len(find_by_author(lib, "Orwell")) == 2
    assert len(find_by_author(lib, "None")) == 0
    assert len(books_before_year(lib, 1946)) == 2
    assert len(books_before_year(lib, 1900)) == 0
    print("All tests passed!")
