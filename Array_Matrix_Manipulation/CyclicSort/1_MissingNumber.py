"""
Missing Number (LeetCode #268)
===============================
Problem:
    Given an array of n distinct numbers in [0, n], return the one missing.

    Input:  nums = [3, 0, 1]  →  2

Logic — Cyclic Sort:
    Place each value at its "correct" index (value i → index i).
    Skip if value == n (no index n) or already in place.
    After sorting, scan — the index whose value ≠ index is the answer.
    If every index matches, n itself is missing.

Time:  O(n) — each element swapped at most once + one scan
Space: O(1)
"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)

        while i < n:
            correct = nums[i]                          # where nums[i] should sit

            if nums[i] < n and nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]  # swap into place
            else:
                i += 1                                 # already correct or value == n

        for i in range(n):                             # find the misplaced index
            if i != nums[i]:
                return i

        return n                                       # 0..n-1 all present → n is missing

    # ---- Clean version (no comments) ----
    def missingNumber_clean(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)

        while i < n:
            correct = nums[i]
            if nums[i] < n and nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1

        for i in range(n):
            if i != nums[i]:
                return i

        return n