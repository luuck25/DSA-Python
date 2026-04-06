"""
Reverse String (LeetCode #344)
===============================
Problem:
    Reverse a character array in-place. Do not allocate extra space.

    Input:  ["h","e","l","l","o"]  →  ["o","l","l","e","h"]

Logic:
    Two pointers at both ends, swap and move inward until they meet.

Time:  O(n)
Space: O(1) — in-place swaps
"""

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        start = 0
        end = len(s) - 1

        while end > start:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    # ---- Clean version (no comments) ----
    def reverseString_clean(self, s: List[str]) -> None:
        start, end = 0, len(s) - 1
        while end > start:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        