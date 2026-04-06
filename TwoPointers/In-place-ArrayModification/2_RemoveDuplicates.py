"""
Remove Duplicates from Sorted Array (LeetCode #26)
====================================================
Problem:
    Sorted array — remove duplicates so each element appears only ONCE.
    Modify in-place, return new length.

    Input:  [1,1,2]  →  2  (nums becomes [1,2,...])

Logic:
    next_unique = write pointer, starts at 1 (first element always safe).
    Scan from index 1: if nums[i] != nums[i-1] → new value found → write it.

Time:  O(n)
Space: O(1)
"""


class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        next_unique = 1  # first element always valid

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:          # new value found
                nums[next_unique] = nums[i]      # write to result position
                next_unique += 1

        return next_unique  # everything before next_unique is unique

    # ---- Clean version (no comments) ----
    def removeDuplicates_clean(self, nums):
        if not nums:
            return 0
        next_unique = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[next_unique] = nums[i]
                next_unique += 1
        return next_unique