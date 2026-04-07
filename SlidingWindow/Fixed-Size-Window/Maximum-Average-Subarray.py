"""
Maximum Average Subarray I (LeetCode #643)
============================================
Problem:
    Given an integer array and a window size k, find the contiguous subarray
    of length k with the maximum average. Return the average.

    Input:  nums = [1,12,-5,-6,50,3], k = 4  →  12.75  (subarray [12,-5,-6,50])

Logic:
    Fixed-size sliding window.
    Expand right adding to sum. Once window exceeds k → slide left out.
    When window == k → check if current average is the max.

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        curr_sum = 0
        max_avg = float('-inf')

        for right in range(len(nums)):
            curr_sum += nums[right]                    # expand — add right element

            if right - left + 1 > k:                   # window too big — slide left out
                curr_sum -= nums[left]
                left += 1

            if right - left + 1 == k:                  # window exactly k — record avg
                max_avg = max(max_avg, curr_sum / k)

        return max_avg

    # ---- Clean version (no comments) ----
    def findMaxAverage_clean(self, nums: List[int], k: int) -> float:
        left = 0
        curr_sum = 0
        max_avg = float('-inf')

        for right in range(len(nums)):
            curr_sum += nums[right]

            if right - left + 1 > k:
                curr_sum -= nums[left]
                left += 1

            if right - left + 1 == k:
                max_avg = max(max_avg, curr_sum / k)

        return max_avg