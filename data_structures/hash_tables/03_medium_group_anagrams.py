"""
HASH TABLES - MEDIUM 1: Group Anagrams
Hint: anagrams are the same when sorted, so use sorted(str) as dict key

Write a function group_anagrams(words) that groups anagrams together.
Return a list of groups. Order of groups and within groups doesn't matter.

Examples:
  group_anagrams(["eat","tea","tan","ate","nat","bat"])
  -> [["bat"], ["nat","tan"], ["ate","eat","tea"]]
"""

# ---- YOUR CODE HERE ----



# ---- TESTS ----
if __name__ == "__main__":
    tests = [
        ([], []),
        (["eat", "tea", "tan", "ate", "nat", "bat"],
         [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ]
    for words, expected in tests:
        result = group_anagrams(words)
        result_sorted = sorted([sorted(g) for g in result])
        expected_sorted = sorted([sorted(g) for g in expected])
        ok = result_sorted == expected_sorted
        print(f"group_anagrams({words!r}) = {result!r}  {'OK' if ok else 'FAIL'}")
