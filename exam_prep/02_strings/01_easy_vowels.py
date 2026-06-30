"""
STRINGS - EASY 1: Count Vowels
Hint: check each character against a set of vowels

Write a function count_vowels(s) that returns the number of vowels
(a, e, i, o, u — case-insensitive) in the string.

Examples:
  count_vowels("hello")  -> 2
  count_vowels("Python") -> 1
"""

def count_vowels(s):
    pass


if __name__ == "__main__":
    assert count_vowels("") == 0
    assert count_vowels("hello") == 2
    assert count_vowels("Python") == 1
    assert count_vowels("AEIOU") == 5
    assert count_vowels("bcdfg") == 0
    print("All tests passed!")
