"""
STRINGS - HARD: Toggle Case (without .swapcase())
Hint: 'a' - 'A' = 32 in ASCII; check uppercase/lowercase ranges

Write a function toggle_case(s) that returns a new string where every
uppercase letter becomes lowercase and every lowercase becomes uppercase.
Non-alphabetic characters stay unchanged.
Do NOT use .swapcase() or .upper() / .lower() on the whole string.

Examples:
  toggle_case("Hello World") -> "hELLO wORLD"
  toggle_case("ABC123")      -> "abc123"
"""

def toggle_case(s):
    pass


if __name__ == "__main__":
    assert toggle_case("") == ""
    assert toggle_case("Hello World") == "hELLO wORLD"
    assert toggle_case("ABC123") == "abc123"
    assert toggle_case("abc") == "ABC"
    assert toggle_case("ABCD") == "abcd"
    print("All tests passed!")
