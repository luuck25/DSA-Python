"""
Search in Rotated Sorted Array II (with duplicates)

Description:
Given a rotated sorted array that may contain duplicates, determine if a target value exists.
Return True if found, False otherwise.
This is a follow-up to "Search in Rotated Sorted Array" where duplicates are allowed.

Example:
    Input: nums = [2,5,6,0,0,1,2], target = 0
    Output: True
    
    Input: nums = [2,5,6,0,0,1,2], target = 3
    Output: False

Approach:
1. Use modified binary search to handle duplicates
2. Special case: When nums[left] == nums[mid] == nums[right], we can't determine which half is sorted
   - Shrink search space: left++, right-- (worst case becomes O(n))
3. If left half is sorted (nums[left] <= nums[mid]):
   - If target is in range [nums[left], nums[mid]), search left
   - Otherwise, search right
4. If right half is sorted:
   - If target is in range (nums[mid], nums[right]], search right
   - Otherwise, search left
5. Return True if found, False otherwise

Time Complexity: O(log n) average case, O(n) worst case when all elements are duplicates
Space Complexity: O(1) - Only using constant extra space for pointers
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            # Cannot determine which half is sorted
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1

            # Left half is sorted
            elif nums[left] <= nums[mid]:

                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Right half is sorted
            else:

                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False


"""
Pseudocode:
-----------
function search(nums, target):
    left = 0
    right = length(nums) - 1
    
    while left <= right:
        mid = (left + right) / 2
        
        if nums[mid] == target:
            return True
        
        // Handle duplicates - can't determine sorted half
        if nums[left] == nums[mid] == nums[right]:
            left = left + 1
            right = right - 1
            continue
        
        // Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        // Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return False
"""