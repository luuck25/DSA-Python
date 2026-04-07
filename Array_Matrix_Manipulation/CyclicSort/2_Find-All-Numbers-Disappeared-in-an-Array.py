"""
Find All Numbers Disappeared in an Array (LeetCode #448)
=========================================================
Problem:
    Given an array of n integers where each is in [1, n], return all numbers
    in [1, n] that do not appear.

    Input:  nums = [4,3,2,7,8,2,3,1]  →  [5, 6]

Logic — Cyclic Sort:
    Place value v at index v−1.  (values are 1-based, indices 0-based)
    No bounds check needed — every value is already in [1, n].
    After sorting, any index where nums[i] ≠ i+1 means i+1 is missing.

    Difference from Missing Number (#268):
        #268 has values [0, n] in size-n array → need nums[i] < n guard.
        Here values are [1, n] in size-n array → every value has a valid slot.

Time:  O(n) — each element swapped at most once + one scan
Space: O(1) — (not counting result list)
"""

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)

        while i < n:
            correct = nums[i] - 1                     # value v belongs at index v-1

            if nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]  # swap into place
            else:
                i += 1                                 # already correct or duplicate

        result = []
        for i in range(n):                             # scan for mismatches
            if i + 1 != nums[i]:
                result.append(i + 1)                   # i+1 is missing

        return result

    # ---- Clean version (no comments) ----
    def findDisappearedNumbers_clean(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)

        while i < n:
            correct = nums[i] - 1
            if nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1

        result = []
        for i in range(n):
            if i + 1 != nums[i]:
                result.append(i + 1)

        return result