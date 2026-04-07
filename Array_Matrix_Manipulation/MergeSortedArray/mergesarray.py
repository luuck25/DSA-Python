"""
Merge Sorted Array (LeetCode #88)
===================================
Problem:
    Two sorted arrays — nums1 (size m+n, last n slots are 0) and nums2 (size n).
    Merge nums2 into nums1 in-place, sorted.

    Input:  nums1 = [1,2,3,0,0,0], m=3, nums2 = [2,5,6], n=3
    Output: nums1 = [1,2,2,3,5,6]

Logic:
    Fill from the BACK. Compare largest of both arrays,
    place the bigger one at the end of nums1, move that pointer left.
    Loop until all of nums2 is placed (if nums1 elements remain, they're already in place).

Time:  O(m + n)
Space: O(1)
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0:
            return

        i = m - 1          # last real element in nums1
        j = n - 1          # last element in nums2
        nex_ele = m + n - 1  # fill position (back of nums1)

        while j >= 0:  # only need to place all of nums2
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[nex_ele] = nums1[i]  # nums1's element is bigger → place it
                i -= 1
            else:
                nums1[nex_ele] = nums2[j]  # nums2's element is bigger (or i exhausted)
                j -= 1
            nex_ele -= 1

    # ---- Clean version (no comments) ----
    def merge_clean(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0:
            return
        i, j, nex_ele = m - 1, n - 1, m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[nex_ele] = nums1[i]
                i -= 1
            else:
                nums1[nex_ele] = nums2[j]
                j -= 1
            nex_ele -= 1

