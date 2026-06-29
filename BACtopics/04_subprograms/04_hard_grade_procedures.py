"""
SUBPROGRAMS - HARD: Procedure with Side Effects
Hint: use a global list, procedures modify it

You are simulating a BAC-style grade management program.
Write:
  1. init_grades() — resets grades to empty list
  2. add_grade(g) — appends grade to grades list
  3. average() — returns the average of all grades, or 0 if empty
  4. above_average() — returns list of grades > average

The grades list is global (module-level variable).

Examples:
  init_grades()
  add_grade(10); add_grade(20); add_grade(30)
  average() -> 20.0
  above_average() -> [30]
"""

grades = []

def init_grades():
    pass

def add_grade(g):
    pass

def average():
    pass

def above_average():
    pass


if __name__ == "__main__":
    init_grades()
    assert grades == []
    add_grade(10)
    add_grade(20)
    add_grade(30)
    assert average() == 20.0
    assert above_average() == [30]
    print("All tests passed!")
