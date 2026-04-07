"""
Max Consecutive Ones III (LeetCode #1004)
==========================================
Problem:
    Binary array — return the longest subarray of 1s if you can flip at most k zeros.

    Input:  nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2  →  6
    (Flip two 0s in [0,0,0,1,1,1,1,0] → [1,1,1,1,1,1])

Logic:
    Sliding window. Expand right — count flipped zeros.
    If flipped > k → shrink left until flipped ≤ k again.
    Track max window size.

Time:  O(n) — each element added/removed at most once
Space: O(1)
"""

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        changed = 0                      # count of 0s flipped in current window
        max_subarray = float('-inf')

        for right in range(len(nums)):
            if nums[right] == 0:
                changed += 1             # flip this 0

            while changed > k:           # too many flips → shrink
                if nums[left] == 0:
                    changed -= 1         # un-flip the leftmost 0
                left += 1

            max_subarray = max(max_subarray, right - left + 1)  # record window size

        return max_subarray

    # ---- Clean version (no comments) ----
    def longestOnes_clean(self, nums: List[int], k: int) -> int:
        left = 0
        changed = 0
        max_subarray = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                changed += 1
            while changed > k:
                if nums[left] == 0:
                    changed -= 1
                left += 1
            max_subarray = max(max_subarray, right - left + 1)

        return max_subarray