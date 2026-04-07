"""
First Missing Positive (LeetCode #41)
======================================
Problem:
    Given an unsorted integer array, return the smallest missing positive integer.
    Must run in O(n) time and O(1) extra space.

    Input:  nums = [3, 4, -1, 1]  →  2

Logic — Cyclic Sort:
    The answer is always in [1, n+1].
    Place value v at index v−1 (only if 1 ≤ v ≤ n).
    Skip negatives, zeros, out-of-range, and duplicates.
    After sorting, first index where nums[i] ≠ i+1 → return i+1.
    If all match, return n+1.

Time:  O(n) — each element swapped at most once + one scan
Space: O(1)
"""

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)

        while i < n:
            correct = nums[i] - 1                     # target index for value nums[i]

            if 1 <= nums[i] <= n and nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]  # swap into place
            else:
                i += 1                                 # skip negatives, out-of-range, duplicates

        for i in range(n):                             # find first mismatch
            if nums[i] != i + 1:
                return i + 1                           # smallest missing positive

        return n + 1                                   # 1..n all present

    # ---- Clean version (no comments) ----
    def firstMissingPositive_clean(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)

        while i < n:
            correct = nums[i] - 1
            if 1 <= nums[i] <= n and nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1