"""
Search in Rotated Sorted Array

Description:
Given a rotated sorted array of unique elements and a target value, return the index of the target.
If not found, return -1. The array was originally sorted in ascending order and rotated at some pivot.
Must run in O(log n) time.

Example:
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4
    
    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1

Approach:
1. Use binary search with modification to handle rotation
2. At each mid point, determine which half is properly sorted
3. If nums[mid] >= nums[left], left half is sorted:
   - If target is in range [nums[left], nums[mid]), search left
   - Otherwise, search right
4. If right half is sorted:
   - If target is in range (nums[mid], nums[right]], search right
   - Otherwise, search left
5. Continue until target is found or search space is exhausted

Time Complexity: O(log n) - Binary search on rotated array
Space Complexity: O(1) - Only using constant extra space for pointers
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) //2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left] :
                # left array is sorted

                if nums[left] <= target < nums[mid]:
                    right = mid -1
                else:
                    left = mid +1    
            else:
                # right arry is sorted
                
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1                     
        return -1              
        
        