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


"""
Plain English Pseudocode:
-------------------------
1. Initialize two pointers: left at start (index 0) and right at end (last index)

2. While the search space has more than one element (left < right):
   - Calculate the middle index between left and right
   
   - Compare the middle element with the rightmost element:
     
     If middle element is GREATER than right element:
       → The rotation pivot (minimum) is in the right half
       → Move left pointer to mid + 1 (exclude mid, it can't be minimum)
     
     Otherwise (middle element is LESS than right element):
       → The rotation pivot (minimum) is at mid or in the left half
       → Move right pointer to mid (include mid, it could be the minimum)
       → Note: Can't be EQUAL since all elements are unique

3. When left equals right, we've converged on the minimum element
   Return the element at left pointer
   
Note: We compare with nums[right] (not nums[left]) because in a rotated array,
      the right side tells us if we're in the rotated portion or not.
"""