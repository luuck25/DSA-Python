"""
Rotate Array (LeetCode #189)
==============================
Problem:
    Rotate array to the right by k steps, in-place.

    Input:  [1,2,3,4,5,6,7], k=3  →  [5,6,7,1,2,3,4]

Logic (3 reverses):
    k = k % n  (rotating n times = same array, so handle k > n)
    1. Reverse entire array     → [7,6,5,4,3,2,1]
    2. Reverse first k elements → [5,6,7,4,3,2,1]
    3. Reverse remaining n-k    → [5,6,7,1,2,3,4]

    Same trick as Reverse Words — reverse whole, then reverse parts.

Time:  O(n)
Space: O(1)

https://www.youtube.com/watch?v=BHr381Guz3Y

"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # if k > n, rotating n times gives same array

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, n - 1)   # Step 1: reverse whole array
        reverse(0, k - 1)   # Step 2: reverse first k elements
        reverse(k, n - 1)   # Step 3: reverse the rest

    # ---- Clean version (no comments) ----
    def rotate_clean(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)