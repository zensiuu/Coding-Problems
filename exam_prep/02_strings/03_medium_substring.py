"""
STRINGS - MEDIUM 1: Substring Search
Hint: slide a window of length len(sub) across s

Write a function find_substring(s, sub) that returns the starting index
of the first occurrence of sub in s, or -1 if not found.
Do NOT use Python's built-in .find() or .index().

Examples:
  find_substring("hello world", "world") -> 6
  find_substring("hello", "xyz")        -> -1
"""

def find_substring(s, sub):
    pass


if __name__ == "__main__":
    assert find_substring("hello world", "world") == 6
    assert find_substring("hello", "xyz") == -1
    assert find_substring("test", "") == 0
    assert find_substring("aaaa", "aa") == 0
    assert find_substring("abc", "c") == 2
    print("All tests passed!")
