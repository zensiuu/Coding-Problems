"""
BASE CONVERSION - EASY 2: Binary to Decimal
Hint: for each digit, result = result*2 + int(digit)

Write a function bin_to_dec(b) that converts a binary string to a
decimal integer. Do NOT use int(b, 2).

Examples:
  bin_to_dec("0")    -> 0
  bin_to_dec("1010") -> 10
  bin_to_dec("11111111") -> 255
"""

def bin_to_dec(b):
    pass


if __name__ == "__main__":
    assert bin_to_dec("0") == 0
    assert bin_to_dec("1") == 1
    assert bin_to_dec("1010") == 10
    assert bin_to_dec("11111111") == 255
    print("All tests passed!")
