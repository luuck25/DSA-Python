"""
Find First and Last Position of Element in Sorted Array

Description:
Given a sorted array of integers, find the starting and ending position of a given target value.
If the target is not found in the array, return [-1, -1].
Must run in O(log n) time complexity.

Example:
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]

Approach:
1. Perform two separate binary searches:
   - First search: Find the leftmost (first) occurrence
     When target is found, continue searching left (right = mid - 1)
   - Second search: Find the rightmost (last) occurrence
     When target is found, continue searching right (left = mid + 1)
2. For each search, maintain a result variable to track the found position
3. Return [first, last] as the result

Time Complexity: O(log n) - Two binary searches (one for first, one for last position)
Space Complexity: O(1) - Only using constant extra space for pointers
"""

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        first = -1


        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                first = mid
                right = mid - 1
  
                
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        left = 0    
        right = len(nums) - 1
        last = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                last = mid
                left = mid + 1
  
                
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return [first,last]        


       
        