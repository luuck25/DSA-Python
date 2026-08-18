"""  
Search Insert Position

Description:
Given a sorted array and a target value, return the index if the target is found.
If not found, return the index where it would be inserted in order.

Example:
    Input: nums = [1,3,5,6], target = 5
    Output: 2
    
    Input: nums = [1,3,5,6], target = 2
    Output: 1

Approach:
1. Use standard binary search with left and right pointers
2. At each iteration, calculate mid = (left + right) // 2
3. If nums[mid] == target, return mid (target found)
4. If nums[mid] > target, search left half (right = mid - 1)
5. If nums[mid] < target, search right half (left = mid + 1)
6. When loop exits, left pointer is at the insertion position
7. Return left as the position where target should be inserted

Time Complexity: O(log n) - Binary search to find target or insertion position
Space Complexity: O(1) - Only using constant extra space for pointers
"""

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
 

        return left                  