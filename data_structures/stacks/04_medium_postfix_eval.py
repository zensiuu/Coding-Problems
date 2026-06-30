"""
STACKS - MEDIUM 2: Evaluate Postfix (Reverse Polish Notation)
Hint: push numbers. When you see an operator, pop two numbers, apply, push result.

Operators: +, -, *, /
Division truncates toward zero (use int(a / b)).

Examples:
  eval_postfix(["2","1","+","3","*"])       -> 9
  eval_postfix(["4","13","5","/","+"])      -> 6
"""

# ---- YOUR CODE HERE ----



# ---- TESTS ----
if __name__ == "__main__":
    tests = [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
        (["5"], 5),
        (["3", "4", "+"], 7),
    ]
    for tokens, expected in tests:
        result = eval_postfix(tokens)
        ok = result == expected
        print(f"eval_postfix({tokens!r}) = {result}  {'OK' if ok else f'FAIL (expected {expected!r})'}")
