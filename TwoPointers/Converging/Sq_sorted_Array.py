"""
Squares of a Sorted Array (LeetCode #977) — Plain English Walkthrough
======================================================
Problem:
    Given a sorted array (may have negatives), return an array of
    squares of each number, also sorted in non-decreasing order.

    Input:  [-4, -1, 0, 3, 10]
    Output: [0, 1, 9, 16, 100]

Key Insight — Two Pointers from both ends:
    The array is sorted, so the LARGEST squares are at the EDGES
    (big negatives on the left, big positives on the right).

    Compare |start| vs |end|, place the bigger square at the END
    of the result array, and move that pointer inward.

    [-4, -1, 0, 3, 10]
      ↑              ↑
    start           end       ← compare |−4|=4 vs |10|=10
                                 10 wins → result[4] = 100, end--

    [-4, -1, 0, 3, 10]
      ↑          ↑
    start       end           ← |−4|=4 vs |3|=3
                                 4 wins → result[3] = 16, start++

    ...and so on, filling result from right to left.

Time:  O(n) — single pass with two pointers
Space: O(1) — just pointers (result array not counted, it's required output)
"""

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        n = len(nums)
        start = 0
        end = n - 1

        result = [0] * n

        # Fill result from the END (largest square first)
        pos = n - 1
        while end >= start:

            # Whichever edge has the bigger absolute value gets placed next
            if abs(nums[start]) > abs(nums[end]):
                result[pos] = nums[start] ** 2
                start += 1
            else:
                result[pos] = nums[end] ** 2
                end -= 1
            pos -= 1

        return result

    # ---- Clean version (no comments) ----
    def sortedSquares_clean(self, nums: List[int]) -> List[int]:
        n = len(nums)
        start, end = 0, n - 1
        result = [0] * n
        pos = n - 1

        while end >= start:
            if abs(nums[start]) > abs(nums[end]):
                result[pos] = nums[start] ** 2
                start += 1
            else:
                result[pos] = nums[end] ** 2
                end -= 1
            pos -= 1

        return result