"""
FILES - EASY 2: Count Lines
Hint: read all lines, count them

Write a function count_lines(filename) that returns the number of lines
in the file.

Examples:
  If file has:
    line1
    line2
  count_lines("test.txt") -> 2
"""

def count_lines(filename):
    pass


if __name__ == "__main__":
    import os
    fname = "_test_lines.txt"
    with open(fname, "w") as f:
        f.write("a\nb\nc\n")
    assert count_lines(fname) == 3
    os.remove(fname)
    print("All tests passed!")
