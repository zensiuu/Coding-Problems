"""
FILES - MEDIUM 1: Append to File
Hint: open in append mode ("a")

Write two functions:
  1. append_to_file(filename, line) — appends a line to the file
  2. read_lines(filename) — returns a list of all lines (without newline)

Examples:
  append_to_file("test.txt", "new line")
  read_lines("test.txt") returns list of lines
"""

def append_to_file(filename, line):
    pass

def read_lines(filename):
    pass


if __name__ == "__main__":
    import os
    fname = "_test_append.txt"
    with open(fname, "w") as f:
        f.write("first\n")
    append_to_file(fname, "second")
    lines = read_lines(fname)
    assert len(lines) == 2
    assert lines[1] == "second"
    os.remove(fname)
    print("All tests passed!")
