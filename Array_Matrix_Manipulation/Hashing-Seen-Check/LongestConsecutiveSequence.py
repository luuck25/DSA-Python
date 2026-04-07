"""
Longest Consecutive Sequence — Plain English Walkthrough
=========================================================
Problem:
    Given an unsorted array of integers, find the length of the
    longest consecutive elements sequence. Must run in O(n).

    Input:  [100, 4, 200, 1, 3, 2]  →  4  (the sequence [1, 2, 3, 4])
    Input:  [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]  →  9  (0 through 8)

Visual Example:
    Input: [100, 4, 200, 1, 3, 2]

    Step 1: Dump everything into a HashSet for O(1) lookup
            st = {100, 4, 200, 1, 3, 2}

    Step 2: Walk through each number. Only start counting if it's the
            BEGINNING of a streak (i.e., num-1 is NOT in the set).

        num = 100
            Is 99 in set?  NO → 100 is a streak START!
            100 in set? YES → count=1, check 101
            101 in set? NO  → streak ends → length = 1

        num = 4
            Is 3 in set?  YES → 4 is NOT a start → SKIP!

        num = 200
            Is 199 in set? NO → 200 is a streak START!
            200 in set? YES → count=1, check 201
            201 in set? NO  → streak ends → length = 1

        num = 1
            Is 0 in set?  NO → 1 IS a streak START!
            1 in set? YES → count=1, check 2
            2 in set? YES → count=2, check 3
            3 in set? YES → count=3, check 4
            4 in set? YES → count=4, check 5
            5 in set? NO  → streak ends → length = 4 ← LONGEST!

        num = 3
            Is 2 in set?  YES → SKIP!

        num = 2
            Is 1 in set?  YES → SKIP!

    Result: 4 ✅

Key Insight — "if num-1 not in st":
    This one check is what makes it O(n) instead of O(n²).
    Without it, we'd start counting from EVERY number (4 would count 4→5→...).
    With it, we ONLY count from streak beginnings (like 1 in [1,2,3,4]).
    So each number is visited at most TWICE: once in the for loop,
    once inside a while loop. Total = O(n) + O(n) = O(n).

Approach:
    1. Put all numbers in a HashSet (O(1) lookup)
    2. For each number:
       - If num-1 exists → it's mid-streak → skip
       - If num-1 doesn't exist → it's a streak start → count forward
    3. Track the longest streak found

Time:  O(n) — each element touched at most twice
Space: O(n) — the HashSet
"""

from typing import List


# https://www.youtube.com/watch?v=bGw2-Pdg_78


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Build a HashSet of all numbers for O(1) lookup
        st = set()

        # Track the longest streak found so far
        longest = 0

        # Add every number to the set
        for num in nums:
            st.add(num)

        for num in nums:

            # Reset count for this potential streak
            count = 0

            # Is this the START of a streak?
            # i.e., there's no number just before it in the set
            # If num-1 exists, someone earlier already covers this streak
            if num - 1 not in st:

                # Yes! Walk forward counting consecutive numbers
                while num in st:

                    count += 1                        # one more in the streak
                    longest = max(longest, count)     # update best so far
                    num = num + 1                     # check next consecutive

        return longest

    # ---- Clean version (no comments) ----
    def longestConsecutive_clean(self, nums: List[int]) -> int:
        st = set()
        longest = 0

        for num in nums:
            st.add(num)

        for num in nums:
            count = 0
            if num - 1 not in st:
                while num in st:
                    count += 1
                    longest = max(longest, count)
                    num = num + 1

        return longest