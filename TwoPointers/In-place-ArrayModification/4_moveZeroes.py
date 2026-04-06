"""
Move Zeroes (LeetCode #283)
============================
Problem:
    Move all 0s to the end while keeping the order of non-zero elements.
    In-place, no extra array.

    Input:  [0, 1, 0, 3, 12]  →  [1, 3, 12, 0, 0]

Logic:
    start = write pointer for next non-zero position.
    Scan with i: if non-zero → swap with start, advance start.
    All non-zeroes bubble to the front, zeroes naturally end up at the back.

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        start = 0  # points to where next non-zero should go

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[start], nums[i] = nums[i], nums[start]  # swap non-zero to front
                start += 1  # advance write pointer

    # ---- Clean version (no comments) ----
    def moveZeroes_clean(self, nums: List[int]) -> None:
        start = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[start], nums[i] = nums[i], nums[start]
                start += 1