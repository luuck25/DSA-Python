"""
Find Minimum in Rotated Sorted Array

Description:
Given a rotated sorted array of unique elements, find the minimum element.
The array was originally sorted in ascending order and rotated at some pivot.

Example:
    Input: nums = [3,4,5,1,2]
    Output: 1

Approach:
1. Use binary search with left and right pointers
2. Compare nums[mid] with nums[right] at each iteration
3. If nums[mid] > nums[right], minimum is in the right half (left = mid + 1)
4. Otherwise, minimum could be at mid or in the left half (right = mid)
5. When left == right, we've found the minimum element
6. The minimum is always at the rotation pivot point

Time Complexity: O(log n) - Binary search to find the pivot/minimum
Space Complexity: O(1) - Only using constant extra space for pointers
"""

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        while left < right:

            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]                
        