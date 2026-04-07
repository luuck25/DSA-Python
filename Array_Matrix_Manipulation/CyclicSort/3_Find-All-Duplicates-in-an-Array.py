"""
Find All Duplicates in an Array (LeetCode #442)
=================================================
Problem:
    Given an array of n integers where each is in [1, n] and some appear twice,
    return all elements that appear twice.

    Input:  nums = [4,3,2,7,8,2,3,1]  →  [2, 3]

Logic — Cyclic Sort:
    Same sort as Disappeared Numbers (#448): place value v at index v−1.
    After sorting, any index where nums[i] ≠ i+1 means nums[i] is a duplicate
    sitting in the wrong slot.
    (Disappeared returns i+1 — the missing value. This returns nums[i] — the extra value.)

Time:  O(n) — each element swapped at most once + one scan
Space: O(1) — (not counting result list)
"""

from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
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
                result.append(nums[i])                 # nums[i] is the duplicate value

        return result

    # ---- Clean version (no comments) ----
    def findDuplicates_clean(self, nums: List[int]) -> List[int]:
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
                result.append(nums[i])

        return result