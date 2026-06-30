"""
FILES - EASY 1: Write and Read
Hint: use open(filename, "w") to write, open(filename, "r") to read

Write two functions:
  1. write_to_file(filename, content) — writes content string to file
  2. read_file(filename) — returns the full content as a string

Examples:
  write_to_file("test.txt", "Hello BAC!")
  read_file("test.txt") -> "Hello BAC!"
"""

def write_to_file(filename, content):
    pass

def read_file(filename):
    pass


if __name__ == "__main__":
    import os
    fname = "_test_temp.txt"
    write_to_file(fname, "Hello BAC!")
    assert read_file(fname) == "Hello BAC!"
    os.remove(fname)
    print("All tests passed!")
