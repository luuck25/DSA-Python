"""
Minimum Size Subarray Sum (LeetCode #209)
==========================================
Problem:
    Find the smallest contiguous subarray whose sum ≥ target. Return its length.
    Return 0 if no such subarray.

    Input:  target = 7, nums = [2,3,1,2,4,3]  →  2  (subarray [4,3])

Logic:
    Sliding window — expand right to grow sum, shrink left while sum ≥ target.
    Each time sum ≥ target, record window size and try shrinking for a smaller one.

Time:  O(n) — each element added/removed at most once
Space: O(1)
"""

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_window = float('inf')

        for right in range(len(nums)):
            current_sum += nums[right]          # expand window

            while current_sum >= target:        # shrink while valid
                min_window = min(min_window, right - left + 1)  # record size
                current_sum -= nums[left]       # remove leftmost
                left += 1

        return 0 if min_window == float('inf') else min_window

    # ---- Clean version (no comments) ----
    def minSubArrayLen_clean(self, target: int, nums: List[int]) -> int:
        left = 0
        current_sum = 0
        min_window = float('inf')

        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                min_window = min(min_window, right - left + 1)
                current_sum -= nums[left]
                left += 1

        return 0 if min_window == float('inf') else min_window
        