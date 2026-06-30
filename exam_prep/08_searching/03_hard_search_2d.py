"""
SEARCH - HARD: Search in 2D Array
Hint: search each row sequentially

Write a function search_2d(matrix, x) that takes a 2D list (rectangular)
and returns (row, col) of the first occurrence of x, or None if not
found. Search left-to-right, top-to-bottom.

Examples:
  m = [[1,2],[3,4]]
  search_2d(m, 3) -> (1,0)
  search_2d(m, 5) -> None
"""

def search_2d(matrix, x):
    pass


if __name__ == "__main__":
    assert search_2d([[]], 1) is None
    m = [[1,2],[3,4]]
    assert search_2d(m, 3) == (1,0)
    assert search_2d(m, 1) == (0,0)
    assert search_2d(m, 5) is None
    print("All tests passed!")
