"""
Add to Array-Form of Integer (LeetCode #989)
==============================================
Problem:
    Array represents a number. Add integer k to it. Return result as array.

    Input:  num = [1, 2, 0, 0], k = 34  →  [1, 2, 3, 4]  (1200 + 34 = 1234)
    Input:  num = [9, 9], k = 1          →  [1, 0, 0]      (99 + 1 = 100)

Logic:
    Walk from last digit backward, add k into the digit directly.
    k itself acts as the carry — k % 10 gives current digit, k // 10 is the carry.
    After the loop, if k still > 0 → prepend remaining digits.

Time:  O(max(n, log k)) — n = array length, log k = digits in k
Space: O(1) — modifies in-place (except prepend for overflow)
"""

from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = len(num)

        for i in range(n - 1, -1, -1):  # walk right to left
            k += num[i]          # absorb digit into k
            num[i] = k % 10     # last digit stays here
            k //= 10            # rest becomes carry

        # If k still has digits left (e.g. 99 + 999 → overflow)
        while k > 0:
            num.insert(0, k % 10)  # prepend remaining digits
            k //= 10

        return num

    # ---- Clean version (no comments) ----
    def addToArrayForm_clean(self, num: List[int], k: int) -> List[int]:
        for i in range(len(num) - 1, -1, -1):
            k += num[i]
            num[i] = k % 10
            k //= 10
        while k > 0:
            num.insert(0, k % 10)
            k //= 10
        return num