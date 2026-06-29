"""
SORTING - HARD: Sort Using a Stable Algorithm
Hint: for equal keys, original order must be preserved

You have a list of (name, score) tuples. Write a function
stable_sort(records) that sorts by score ascending using a stable
sorting algorithm (not Python's built-in sort).
Implement insertion sort — it's naturally stable.

Examples:
  data = [("A",3), ("B",1), ("C",3)]
  stable_sort(data) -> [("B",1), ("A",3), ("C",3)]
  # A comes before C because A appeared first
"""

def stable_sort(records):
    pass


if __name__ == "__main__":
    data = [("A",3), ("B",1), ("C",3)]
    result = stable_sort(data)
    assert result[0] == ("B",1)
    assert result[1] == ("A",3)
    assert result[2] == ("C",3)
    print("All tests passed!")
