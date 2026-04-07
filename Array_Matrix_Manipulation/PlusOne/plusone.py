"""
Plus One (LeetCode #66)
========================
Problem:
    Array represents a large integer (each element is a digit).
    Add 1 to the number and return the result as an array.

    Input:  [1, 2, 9]  →  [1, 3, 0]
    Input:  [9, 9, 9]  →  [1, 0, 0, 0]

Logic:
    Walk from the last digit backward:
      - If digit < 9 → just increment and return (no carry).
      - If digit == 9 → set to 0, carry propagates left.
    If loop finishes → all digits were 9 (e.g. 999 → 000) → prepend 1.

Time:  O(n)
Space: O(1) — modifies in-place (except the all-9s case: O(n) for new array)
"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits) - 1, -1, -1):  # walk right to left
            if digits[i] < 9:
                digits[i] = digits[i] + 1  # no carry needed, done
                return digits
            digits[i] = 0  # 9 → 0, carry propagates

        # If we're here, all digits were 9 (e.g. [9,9,9] → [0,0,0])
        return [1] + digits

    # ---- Clean version (no comments) ----
    def plusOne_clean(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits