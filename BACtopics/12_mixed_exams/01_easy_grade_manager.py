"""
MIXED EXAMS - EASY: Student Grade Manager
Hint: combine records + arrays + average computation

A class has 10 students. Each student has a name and a grade.
Write functions to:
  1. add_student(name, grade) — adds to a global list
  2. class_average() — returns average of all grades
  3. above_average_students() — returns list of names above average
  4. max_grade() — returns the highest grade

Examples:
  add_student("Ali", 15); add_student("Sara", 17)
  class_average() -> 16.0
  above_average_students() -> ["Sara"]
"""

students = []

def reset():
    students.clear()

def add_student(name, grade):
    pass

def class_average():
    pass

def above_average_students():
    pass

def max_grade():
    pass


if __name__ == "__main__":
    reset()
    add_student("Ali", 15)
    add_student("Sara", 17)
    add_student("Mehdi", 14)
    assert class_average() == (15+17+14)/3
    assert above_average_students() == ["Sara"]
    assert max_grade() == 17
    print("All tests passed!")
