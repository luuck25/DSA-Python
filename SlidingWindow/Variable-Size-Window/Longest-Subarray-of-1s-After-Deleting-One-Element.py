"""
Longest Subarray of 1's After Deleting One Element (LeetCode #1493)
====================================================================
Problem:
    Given a binary array, return the longest subarray of 1s after deleting
    exactly one element (you MUST delete one).

    Input:  nums = [1,1,0,1,1,1,0,1,1]  →  5
    (Delete the 0 at index 2 → [1,1,1,1,1])

Logic:
    Sliding window allowing at most one 0 (the "deleted" element).
    Expand right — if 0 found, increment deleted count.
    If deleted > 1 → shrink left until deleted ≤ 1.
    Window length is right − left (not +1, because one element is deleted).

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        deleted = 0                                # count of 0s in window (max 1 allowed)
        result = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                deleted += 1

                while deleted > 1:                 # too many 0s → shrink
                    if nums[left] == 0:
                        deleted -= 1
                    left += 1

            result = max(result, right - left)     # right - left (not +1) → one element deleted

        return result

    # ---- Clean version (no comments) ----
    def longestSubarray_clean(self, nums: List[int]) -> int:
        left = 0
        deleted = 0
        result = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                deleted += 1
                while deleted > 1:
                    if nums[left] == 0:
                        deleted -= 1
                    left += 1

            result = max(result, right - left)

        return result
