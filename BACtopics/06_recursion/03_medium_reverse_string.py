"""
RECURSION - MEDIUM 1: Reverse String (Recursive)
Hint: s[-1] + reverse(s[:-1]), base case s == ""

Write a recursive function reverse_rec(s) that returns the reversed
version of string s.

Examples:
  reverse_rec("hello") -> "olleh"
  reverse_rec("")      -> ""
"""

def reverse_rec(s):
    pass


if __name__ == "__main__":
    assert reverse_rec("") == ""
    assert reverse_rec("a") == "a"
    assert reverse_rec("hello") == "olleh"
    assert reverse_rec("racecar") == "racecar"
    print("All tests passed!")
