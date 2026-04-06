"""
Remove Duplicates from Sorted Array II (LeetCode #80)
======================================================
Problem:
    Sorted array — remove duplicates so each element appears at most TWICE.
    Modify in-place, return new length.

    Input:  [1,1,1,2,2,3]  →  5  (nums becomes [1,1,2,2,3,...])

Logic:
    next_unique = write pointer, starts at 2 (first 2 elements always safe).
    For each element from index 2 onward:
      Compare nums[i] with nums[next_unique - 2] (the element 2 positions back in the result).
      If different → it's safe to keep (at most 2 of this value so far) → write it.

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        next_unique = 2  # first 2 elements always valid

        for i in range(2, len(nums)):
            # compare with 2 positions back — if same, we already have 2 copies
            if nums[i] != nums[next_unique - 2]:
                nums[next_unique] = nums[i]  # write to result position
                next_unique += 1

        return next_unique

    # ---- Clean version (no comments) ----
    def removeDuplicates_clean(self, nums: List[int]) -> int:
        next_unique = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[next_unique - 2]:
                nums[next_unique] = nums[i]
                next_unique += 1
        return next_unique