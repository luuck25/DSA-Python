"""
Split Array Largest Sum (LeetCode #410)
========================================
Problem:
    Split nums into k non-empty contiguous subarrays so that the largest
    subarray sum among them is minimized. Return that minimized largest sum.

    Input:  nums = [7,2,5,10,8], k = 2  →  18
    (Split [7,2,5] and [10,8] → sums 14, 18 → max is 18, which is optimal)

Logic:
    Binary search on the answer (the max-subarray-sum).
    • low  = max(nums)  — at minimum each subarray holds one element
    • high = sum(nums)   — one subarray holds everything
    • For a candidate mid, greedily count how many subarrays are needed
      (pack elements until sum > mid, then start a new subarray).
    • If subarrays needed > k → mid too small → search right.
    • Otherwise → mid is feasible → search left for a smaller answer.

Time:  O(n · log(sum − max))  — binary search × linear scan
Space: O(1)

Reference: https://www.youtube.com/watch?v=Z0hwjftStI4
"""

from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def countSubarray(nums, elementSum):
            """Count subarrays needed if each subarray sum ≤ elementSum."""
            num_subarray = 1                        # start with one subarray
            curr_sum = 0

            for i in range(len(nums)):
                if curr_sum + nums[i] <= elementSum:
                    curr_sum += nums[i]             # fits — keep packing
                else:
                    curr_sum = nums[i]              # doesn't fit — start new subarray
                    num_subarray += 1

            return num_subarray

        low = max(nums)                             # smallest possible answer
        high = sum(nums)                            # largest possible answer

        while low <= high:
            mid = low + (high - low) // 2           # candidate max-subarray-sum

            subarray = countSubarray(nums, mid)

            if subarray > k:                        # need too many splits → raise floor
                low = mid + 1
            else:                                   # feasible → try smaller
                high = mid - 1

        return low                                  # first feasible value

    # ---- Clean version (no comments) ----
    def splitArray_clean(self, nums: List[int], k: int) -> int:

        def countSubarray(nums, elementSum):
            num_subarray = 1
            curr_sum = 0
            for i in range(len(nums)):
                if curr_sum + nums[i] <= elementSum:
                    curr_sum += nums[i]
                else:
                    curr_sum = nums[i]
                    num_subarray += 1
            return num_subarray

        low = max(nums)
        high = sum(nums)

        while low <= high:
            mid = low + (high - low) // 2
            subarray = countSubarray(nums, mid)
            if subarray > k:
                low = mid + 1
            else:
                high = mid - 1

        return low