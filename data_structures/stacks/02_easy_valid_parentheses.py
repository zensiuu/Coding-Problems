"""
STACKS - EASY 2: Valid Parentheses
Hint: push opening brackets, pop and match when you see a closing bracket

Write a function is_valid(s) that determines if the string of brackets
'(', ')', '{', '}', '[', ']' is well-formed.

Examples:
  is_valid("()")      -> True
  is_valid("()[]{}")  -> True
  is_valid("(]")      -> False
  is_valid("([)]")    -> False
"""

# ---- YOUR CODE HERE ----



# ---- TESTS ----
if __name__ == "__main__":
    tests = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("((", False),
        ("))", False),
    ]
    for s, expected in tests:
        result = is_valid(s)
        ok = result == expected
        print(f"is_valid({s!r}) = {result}  {'OK' if ok else f'FAIL (expected {expected!r})'}")
