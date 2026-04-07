"""
Contains Duplicate II (LeetCode #219)
======================================
Problem:
    Return True if there are two distinct indices i, j such that
    nums[i] == nums[j] and abs(i - j) <= k.

    Input:  nums = [1,2,3,1], k = 3  →  True

Logic:
    Sliding window of size k backed by a set.
    Expand right — if window exceeds k, remove leftmost and slide.
    Before adding nums[right], check if it's already in the set → duplicate found.

Time:  O(n)
Space: O(k) — set holds at most k elements
"""

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()                             # values in current window
        left = 0

        for right in range(len(nums)):
            if right - left > k:                   # window exceeds k → shrink
                window.remove(nums[left])
                left += 1

            if nums[right] in window:              # duplicate within distance k
                return True

            window.add(nums[right])                # add current to window

        return False

    # ---- Clean version (no comments) ----
    def containsNearbyDuplicate_clean(self, nums: List[int], k: int) -> bool:
        window = set()
        left = 0

        for right in range(len(nums)):
            if right - left > k:
                window.remove(nums[left])
                left += 1

            if nums[right] in window:
                return True

            window.add(nums[right])

        return False