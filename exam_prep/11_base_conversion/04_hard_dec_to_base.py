"""
BASE CONVERSION - HARD: Decimal to Any Base (2 to 36)
Hint: general algorithm: divide by base, collect remainders

Write a function dec_to_base(n, base) that converts a non-negative
integer to a string in the given base (2 <= base <= 36).
Use digits 0-9 then A-Z for values above 9.
Do NOT use built-in conversion functions.

Examples:
  dec_to_base(255, 16) -> "FF"
  dec_to_base(255, 2)  -> "11111111"
  dec_to_base(35, 36)  -> "Z"
"""

def dec_to_base(n, base):
    pass


if __name__ == "__main__":
    assert dec_to_base(0, 16) == "0"
    assert dec_to_base(255, 16) == "FF"
    assert dec_to_base(255, 2) == "11111111"
    assert dec_to_base(35, 36) == "Z"
    assert dec_to_base(10, 8) == "12"
    print("All tests passed!")
