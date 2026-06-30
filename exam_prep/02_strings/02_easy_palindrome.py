"""
STRINGS - EASY 2: Palindrome
Hint: compare characters from both ends moving inward

Write a function is_palindrome(s) that returns True if s reads the same
forward and backward (case-insensitive, ignore spaces).

Examples:
  is_palindrome("radar")      -> True
  is_palindrome("Race car")   -> True
  is_palindrome("hello")      -> False
"""

def is_palindrome(s):
    pass


if __name__ == "__main__":
    assert is_palindrome("") == True
    assert is_palindrome("radar") == True
    assert is_palindrome("Race car") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("A man a plan a canal Panama") == True
    print("All tests passed!")
