"""
FILES - HARD: Student Grades File
Hint: read lines, split into fields, compute stats

You have a file "grades.txt" where each line is:
  Name,Grade

Write a function process_grades(filename) that reads the file and
returns a dict with:
  - "best": name of student with highest grade
  - "worst": name of student with lowest grade
  - "average": class average (float)
  - "above_avg": list of names above average

If file is empty, return an empty dict.

Examples:
  grades.txt:
    Ali,15
    Sara,17
    Mehdi,14
  result["best"] -> "Sara"
"""

def process_grades(filename):
    pass


if __name__ == "__main__":
    import os
    fname = "_test_grades.txt"
    with open(fname, "w") as f:
        f.write("Ali,15\nSara,17\nMehdi,14\n")
    result = process_grades(fname)
    assert result["best"] == "Sara"
    assert result["worst"] == "Mehdi"
    assert result["average"] == (15+17+14)/3
    assert "Ali" in result["above_avg"]
    os.remove(fname)
    print("All tests passed!")
