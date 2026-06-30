"""
RECORDS - EASY 2: Find Best Student
Hint: loop through records, track the highest grade

Write a function best_student(students) that takes a list of student
records (dicts with "name" and "grade") and returns the name of the
student with the highest grade. If tie, return the first encountered.

Examples:
  students = [
    {"name": "Ali", "grade": 14},
    {"name": "Sara", "grade": 17},
    {"name": "Mehdi", "grade": 15}
  ]
  best_student(students) -> "Sara"
"""

def best_student(students):
    pass


if __name__ == "__main__":
    assert best_student([]) is None
    assert best_student([{"name": "A", "grade": 10}]) == "A"
    students = [
        {"name": "Ali", "grade": 14},
        {"name": "Sara", "grade": 17},
        {"name": "Mehdi", "grade": 15}
    ]
    assert best_student(students) == "Sara"
    print("All tests passed!")
