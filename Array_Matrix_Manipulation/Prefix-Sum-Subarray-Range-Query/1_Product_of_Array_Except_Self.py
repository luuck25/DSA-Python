"""
Product of Array Except Self (LeetCode #238)
==============================================
Problem:
    Return an array where each element is the product of all other elements.
    No division allowed.

    Input:  [1, 2, 3, 4]  →  [24, 12, 8, 6]

Logic:
    Two passes — build prefix products, then multiply by suffix products.

    Pass 1 (left → right): res[i] = product of everything LEFT of i
        nums:   [1,  2,  3,  4]
        res:    [1,  1,  2,  6]   ← prefix before each element

    Pass 2 (right → left): multiply res[i] by product of everything RIGHT of i
        res:    [24, 12, 8,  6]   ← prefix × suffix = answer

Time:  O(n) — two passes
Space: O(1) — result array is required output, only extra is prefix/postfix vars
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        # Pass 1: prefix products (product of all elements to the LEFT)
        prefix = 1
        for num in nums:
            res.append(prefix)     # store prefix so far (excludes current)
            prefix = prefix * num  # update prefix to include current

        # Pass 2: multiply by suffix products (product of all elements to the RIGHT)
        n = len(nums)
        postfix = 1
        for i in range(n - 1, -1, -1):
            res[i] = res[i] * postfix    # prefix × postfix = answer
            postfix = nums[i] * postfix  # update postfix to include current

        return res

    # ---- Clean version (no comments) ----
    def productExceptSelf_clean(self, nums: List[int]) -> List[int]:
        res = []
        prefix = 1
        for num in nums:
            res.append(prefix)
            prefix *= num

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
        