"""
Minimum Operations to Reduce X to Zero (LeetCode #1658)
=========================================================
Problem:
    Remove elements from the left or right end of the array so their sum == x.
    Return the minimum number of operations, or -1 if impossible.

    Input:  nums = [1,1,4,2,3], x = 5  →  2  (remove 3 + 2 from right)

Logic:
    Flip the problem: instead of minimizing elements removed from edges,
    maximize the length of a middle subarray whose sum == total − x.
    Sliding window finds the longest subarray with sum == target.
    Answer = n − max_len.

    Edge cases:
        target < 0  → impossible (x > total sum)
        target == 0 → remove everything

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x                     # sum of the middle subarray we want

        if target < 0:                             # x exceeds total → impossible
            return -1
        if target == 0:                            # entire array must be removed
            return len(nums)

        left = 0
        curr_sum = 0
        max_len = -1                               # longest middle subarray with sum == target

        for right in range(len(nums)):
            curr_sum += nums[right]                # expand window

            while curr_sum > target:               # too big → shrink left
                curr_sum -= nums[left]
                left += 1

            if curr_sum == target:                 # valid middle subarray
                max_len = max(max_len, right - left + 1)

        return len(nums) - max_len if max_len != -1 else -1  # operations = n − middle length

    # ---- Clean version (no comments) ----
    def minOperations_clean(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x

        if target < 0:
            return -1
        if target == 0:
            return len(nums)

        left = 0
        curr_sum = 0
        max_len = -1

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum > target:
                curr_sum -= nums[left]
                left += 1

            if curr_sum == target:
                max_len = max(max_len, right - left + 1)

        return len(nums) - max_len if max_len != -1 else -1