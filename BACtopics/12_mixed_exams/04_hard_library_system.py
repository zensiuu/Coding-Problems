"""
MIXED EXAMS - HARD: Full BAC-Style Library Management System
Hint: combine records + files + sorting + search + subprograms

You are asked to create a library management program.
Each book is a dict: {"id": int, "title": str, "author": str, "year": int, "available": bool}

Write the following program:
  1. load_books(filename) — reads books from a CSV file (id,title,author,year,available)
     and returns a list of book dicts.
  2. save_books(filename, books) — writes books list to CSV.
  3. search_by_title(books, keyword) — returns list of books whose title
     contains the keyword (case-insensitive).
  4. borrow_book(books, book_id) — sets available to False, returns True
     if book exists and was available, else False.
  5. return_book(books, book_id) — sets available to True, returns True
     if book exists.

The CSV format (no header):
  1,1984,George Orwell,1949,True
  2,Brave New World,Aldous Huxley,1932,False

Examples:
  books = load_books("library.csv")
  search_by_title(books, "brave") -> [books[1]]
"""

def load_books(filename):
    pass

def save_books(filename, books):
    pass

def search_by_title(books, keyword):
    pass

def borrow_book(books, book_id):
    pass

def return_book(books, book_id):
    pass


if __name__ == "__main__":
    import os
    fname = "_test_library.csv"
    with open(fname, "w") as f:
        f.write("1,1984,George Orwell,1949,True\n")
        f.write("2,Brave New World,Aldous Huxley,1932,True\n")
    
    books = load_books(fname)
    assert len(books) == 2
    assert books[1]["title"] == "Brave New World"
    
    result = search_by_title(books, "1984")
    assert len(result) == 1
    
    assert borrow_book(books, 1) == True
    assert books[0]["available"] == False
    assert borrow_book(books, 1) == False  # already borrowed
    
    assert return_book(books, 1) == True
    assert books[0]["available"] == True
    
    assert borrow_book(books, 999) == False  # not found
    
    os.remove(fname)
    print("All tests passed!")
