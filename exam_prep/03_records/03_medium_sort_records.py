"""
RECORDS - MEDIUM 1: Sort Students by Grade
Hint: use bubble/selection/insertion sort on grade field

Write a function sort_by_grade(students) that takes a list of student
records (dicts) and returns a NEW sorted list (ascending by grade).
Do NOT use .sort() or sorted().

Examples:
  students = [
    {"name": "Ali", "grade": 14},
    {"name": "Sara", "grade": 17},
    {"name": "Mehdi", "grade": 15}
  ]
  sort_by_grade(students)[0]["name"] -> "Ali"
"""

def sort_by_grade(students):
    pass


if __name__ == "__main__":
    students = [
        {"name": "Ali", "grade": 14},
        {"name": "Sara", "grade": 17},
        {"name": "Mehdi", "grade": 15}
    ]
    result = sort_by_grade(students)
    assert result[0]["name"] == "Ali"
    assert result[1]["name"] == "Mehdi"
    assert result[2]["name"] == "Sara"
    # original unchanged
    assert len(students) == 3
    print("All tests passed!")
