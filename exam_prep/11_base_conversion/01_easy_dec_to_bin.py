"""
BASE CONVERSION - EASY 1: Decimal to Binary
Hint: repeatedly divide by 2, collect remainders in reverse

Write a function dec_to_bin(n) that converts a non-negative integer
n to its binary string representation. n is a Python integer.
Do NOT use bin().

Examples:
  dec_to_bin(0)  -> "0"
  dec_to_bin(10) -> "1010"
"""

def dec_to_bin(n):
    pass


if __name__ == "__main__":
    assert dec_to_bin(0) == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin(10) == "1010"
    assert dec_to_bin(255) == "11111111"
    print("All tests passed!")
