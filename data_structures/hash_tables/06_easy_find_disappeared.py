"""
HASH TABLES - EASY 3: Find All Disappeared Numbers

PROBLEM:
  Given an array nums of n integers where nums[i] is in the range [1, n],
  return an array of all the integers in the range [1, n] that do NOT
  appear in nums.

CONSTRAINTS:
  - n == len(nums)
  - 1 <= nums[i] <= n

EXAMPLES:
  find_disappeared([4,3,2,7,8,2,3,1]) -> [5,6]
  find_disappeared([1,1])             -> [2]
  find_disappeared([1,2,3,4])         -> []

LOGICAL BREAKDOWN:
  The range [1, n] contains exactly n numbers, and the array also has
  exactly n slots. So every number that IS present "takes up" one slot
  in the expected set. The numbers left over are the missing ones.

HINT:
  Use a set for O(1) membership checks. Build a set of what you HAVE,
  then iterate the full range and collect what you DON'T have.

WHY A SET?
  A list membership check is O(n) — scanning the whole list each time.
  A set membership check is O(1) on average (hash table lookup).
  For n elements, that's O(n^2) vs O(n) total — a huge difference at scale.

STEP-BY-STEP (hash set approach):
  1. n = len(nums)
  2. Build a set from nums:  seen = set(nums)
     set(nums) iterates through nums once and inserts each element into a
     hash table. Duplicates are automatically discarded (sets store unique
     values). This is O(n) time and O(n) space.

  3. range(1, n + 1) produces: 1, 2, 3, ..., n
     This is the FULL set of numbers that SHOULD exist.

  4. For each i in that range:
       if i not in seen:  ← O(1) hash lookup
         collect i

  5. Return the collected list.

ALTERNATIVE — In-place marking (O(1) space):
  Since each value v in [1, n] maps uniquely to index v-1, we can use the
  sign bit of each element as a "seen" flag without extra storage:

    for num in nums:
        idx = abs(num) - 1
        if nums[idx] > 0:
            nums[idx] = -nums[idx]   # mark index as "seen"

    return [i + 1 for i in range(n) if nums[i] > 0]
              # positive = never visited = disappeared

  This modifies the input array but uses O(1) extra memory.
"""


def find_disappeared(nums):
    n = len(nums)
    seen = set(nums)
    return [i for i in range(1, n + 1) if i not in seen]


# ---- TESTS ----
if __name__ == "__main__":
    tests = [
        ([4, 3, 2, 7, 8, 2, 3, 1], [5, 6]),
        ([1, 1], [2]),
        ([1, 2, 3, 4], []),
        ([], []),
        ([2, 2, 2, 2], [1, 3, 4]),
    ]
    for nums, expected in tests:
        result = find_disappeared(nums)
        ok = result == expected
        print(f"find_disappeared({nums!r}) = {result!r}  {'OK' if ok else f'FAIL (expected {expected!r})'}")
