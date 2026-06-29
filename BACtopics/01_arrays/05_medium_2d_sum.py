"""
ARRAYS - MEDIUM 2: 2D Array (Matrix) Row Sums
Hint: nested loops, outer row / inner column

Write a function row_sums(matrix) that takes a 2D list (list of lists)
and returns a list where each element is the sum of the corresponding row.

Examples:
  row_sums([[1,2],[3,4]]) -> [3, 7]
  row_sums([[5]])         -> [5]
"""

def row_sums(matrix):
    pass


if __name__ == "__main__":
    assert row_sums([[]]) == [0]
    assert row_sums([[1,2],[3,4]]) == [3, 7]
    assert row_sums([[5]]) == [5]
    assert row_sums([[1,2,3],[4,5,6],[7,8,9]]) == [6, 15, 24]
    print("All tests passed!")
