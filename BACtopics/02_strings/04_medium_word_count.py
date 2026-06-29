"""
STRINGS - MEDIUM 2: Word Count
Hint: split on spaces, handle multiple spaces

Write a function word_count(s) that returns the number of words in the
string. Words are separated by one or more spaces.

Examples:
  word_count("hello world")   -> 2
  word_count("  hi   there ") -> 2
"""

def word_count(s):
    pass


if __name__ == "__main__":
    assert word_count("") == 0
    assert word_count("hello") == 1
    assert word_count("hello world") == 2
    assert word_count("  hi   there ") == 2
    assert word_count("one two three four") == 4
    print("All tests passed!")
