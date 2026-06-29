"""
BASE CONVERSION - MEDIUM 1: Decimal to Hexadecimal
Hint: repeatedly divide by 16, map remainders 10-15 to A-F

Write a function dec_to_hex(n) that converts a non-negative integer
to its hexadecimal string representation. Use uppercase A-F.
Do NOT use hex().

Examples:
  dec_to_hex(0)   -> "0"
  dec_to_hex(255) -> "FF"
  dec_to_hex(16)  -> "10"
"""

def dec_to_hex(n):
    pass


if __name__ == "__main__":
    assert dec_to_hex(0) == "0"
    assert dec_to_hex(10) == "A"
    assert dec_to_hex(16) == "10"
    assert dec_to_hex(255) == "FF"
    assert dec_to_hex(4095) == "FFF"
    print("All tests passed!")
