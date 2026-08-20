"""  
Single Element in a Sorted Array

Description:
Given a sorted array where every element appears exactly twice except for one element
which appears once, find that single element.
Must run in O(log n) time and O(1) space.

Example:
    Input: nums = [1,1,2,3,3,4,4,8,8]
    Output: 2

Approach:
1. Use binary search exploiting the pattern of pairs
2. Key observation: Before the single element, pairs start at even indices
   After the single element, pairs start at odd indices
3. Ensure mid is always at an even index (if odd, decrement by 1)
4. If nums[mid] == nums[mid + 1], single element is on the right (left = mid + 2)
5. Otherwise, single element is on the left or at mid (right = mid)
6. When left == right, we've found the single element

Time Complexity: O(log n) - Binary search utilizing the pattern of pairs
Space Complexity: O(1) - Only using constant extra space for pointers
"""

from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            else:
                right = mid

        return nums[left]


"""
Pseudocode:
-----------
function singleNonDuplicate(nums):
    left = 0
    right = length(nums) - 1
    
    while left < right:
        mid = (left + right) / 2
        
        // Ensure mid is at even index
        if mid is odd:
            mid = mid - 1
        
        // Check if pair starts at mid
        if nums[mid] == nums[mid + 1]:
            left = mid + 2  // Single element is on right
        else:
            right = mid     // Single element is at mid or left
    
    return nums[left]  // Single element
"""