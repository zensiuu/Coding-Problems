"""
RECORDS - EASY 1: Student Record
Hint: a record is a named tuple / dict / simple class

In BAC exams a "record" (enregistrement) groups related data.
Create a function create_student(name, age, grade) that returns a
dictionary representing a student. Also write display_student(s)
that prints the info in a formatted way.

Examples:
  s = create_student("Ahmed", 18, 15.5)
  display_student(s) prints: "Name: Ahmed | Age: 18 | Grade: 15.5"
"""

def create_student(name, age, grade):
    pass

def display_student(s):
    pass


if __name__ == "__main__":
    s = create_student("Ahmed", 18, 15.5)
    assert s["name"] == "Ahmed"
    assert s["age"] == 18
    assert s["grade"] == 15.5
    s2 = create_student("Sarra", 17, 14.0)
    assert s2["name"] == "Sarra"
    print("All tests passed!")
