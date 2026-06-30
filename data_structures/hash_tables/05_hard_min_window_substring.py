"""
HASH TABLES - HARD: Minimum Window Substring
Hint 1: sliding window — expand right until you have all chars, shrink from left
Hint 2: use two dicts (or Counter) to track character counts

Given two strings s and t, return the minimum window substring of s that
contains all characters of t (including duplicates). Return "" if none.

Examples:
  min_window("ADOBECODEBANC", "ABC") -> "BANC"
  min_window("a", "aa")             -> ""
"""

# ---- YOUR CODE HERE ----



# ---- TESTS ----
if __name__ == "__main__":
    tests = [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
        ("aa", "aa", "aa"),
        ("ab", "b", "b"),
        ("abc", "ac", "abc"),
    ]
    for s, t, expected in tests:
        result = min_window(s, t)
        ok = result == expected
        print(f"min_window({s!r}, {t!r}) = {result!r}  {'OK' if ok else f'FAIL (expected {expected!r})'}")
