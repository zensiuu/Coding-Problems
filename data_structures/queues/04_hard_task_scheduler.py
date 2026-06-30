"""
QUEUES - HARD: Task Scheduler
Hint: (max_freq - 1) * (n + 1) + count_of_max_freq_tasks

Given a list of tasks (letters) and a cooling interval n (same task must wait
n cycles before it can repeat), find the minimum number of CPU cycles needed
to finish all tasks. Idle cycles are allowed.

Examples:
  least_interval(["A","A","A","B","B","B"], 2) -> 8
  least_interval(["A","A","A","B","B","B"], 0) -> 6
"""

# ---- YOUR CODE HERE ----



# ---- TESTS ----
if __name__ == "__main__":
    tests = [
        (["A", "A", "A", "B", "B", "B"], 2, 8),
        (["A", "A", "A", "B", "B", "B"], 0, 6),
        (["A", "A", "A", "B", "B", "C", "C"], 1, 7),
        (["A", "A", "A", "B", "B", "B"], 3, 10),
        (["A", "B", "C", "D"], 3, 4),
    ]
    for tasks, n, expected in tests:
        result = least_interval(tasks, n)
        ok = result == expected
        print(f"least_interval({tasks!r}, {n}) = {result}  {'OK' if ok else f'FAIL (expected {expected!r})'}")
