"""
Frequency of the Most Frequent Element (LeetCode #1838)
========================================================
Problem:
    Given an integer array and a budget k, you can increment any element by 1
    (costs 1 per increment). Return the maximum possible frequency of any element.

    Input:  nums = [1,2,4], k = 5  →  3   (increment 1→4, 2→4 → three 4s)

Logic:
    Sort → sliding window.
    Pick nums[right] as the target value for the window.
    Cost to make every element in window equal to target =
        (window_size * target) − actual_sum_of_window   =  window_sum − curr_sum
    If cost > k → shrink left.
    Track max window size.

Time:  O(n log n) — sort dominates
Space: O(1) — (ignoring sort's internal space)

Reference: https://www.youtube.com/watch?v=iOqH_JnXIOQ
"""

from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()                              # sort so we can use a contiguous window
        left = 0
        result = 0
        curr_sum = 0                             # actual sum of elements in window

        for right in range(len(nums)):
            target = nums[right]                 # every element in window should become target
            curr_sum += nums[right]

            window_sum = (right - left + 1) * target  # ideal sum if all equal target

            if window_sum - curr_sum > k:        # cost exceeds budget → shrink
                curr_sum -= nums[left]
                left += 1

            result = max(result, right - left + 1)  # record max frequency

        return result

    # ---- Clean version (no comments) ----
    def maxFrequency_clean(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        result = 0
        curr_sum = 0

        for right in range(len(nums)):
            target = nums[right]
            curr_sum += nums[right]

            window_sum = (right - left + 1) * target

            if window_sum - curr_sum > k:
                curr_sum -= nums[left]
                left += 1

            result = max(result, right - left + 1)

        return result