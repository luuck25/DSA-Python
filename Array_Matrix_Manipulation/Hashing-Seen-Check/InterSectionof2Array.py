"""
Intersection of Two Arrays (LeetCode #349 & #350)
===================================================

#349 — Return unique common elements (use set).
    Input:  [1,2,2,1], [2,2]  →  [2]

#350 — Return all common elements including duplicates (use counter).
    Input:  [1,2,2,1], [2,2]  →  [2,2]
"""

from typing import List
from collections import Counter


class Solution:
    # ---- #349: Unique intersection (set approach) ----
    def intersection_unique(self, nums1, nums2):
        s1 = set(nums1)              # O(n) — dedupe nums1
        result = set()

        for num in nums2:
            if num in s1:             # O(1) lookup
                result.add(num)       # set ensures no duplicates in result

        return list(result)
        # Time: O(n + m)  Space: O(n)

    # ---- #350: Intersection with duplicates (counter approach) ----
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = Counter(nums1)      # count frequencies in nums1
        res = []

        for num in nums2:
            if counter[num] > 0:      # still have this number available
                res.append(num)
                counter[num] -= 1     # use up one occurrence

        return res
        # Time: O(n + m)  Space: O(n)

    # ---- Clean versions (no comments) ----
    def intersection_unique_clean(self, nums1, nums2):
        s1 = set(nums1)
        result = set()
        for num in nums2:
            if num in s1:
                result.add(num)
        return list(result)

    def intersect_clean(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = Counter(nums1)
        res = []
        for num in nums2:
            if counter[num] > 0:
                res.append(num)
                counter[num] -= 1
        return res
