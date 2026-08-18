"""
Search in Rotated Sorted Array

Description:
Given a rotated sorted array and a target value, find the index of the target.
If the target doesn't exist in the array, return -1.
The array was originally sorted in ascending order and then rotated at some pivot.

Example:
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

Approach:
1. Use binary search with two pointers (low and high)
2. At each iteration, determine which half is properly sorted
3. Check if nums[mid] > nums[high] to identify the rotation point
4. If left half is sorted and target is in that range, search left
5. Otherwise, search the right half
6. Continue until target is found or search space is exhausted

Time Complexity: O(log n) - Binary search on the rotated array
Space Complexity: O(1) - Only using constant extra space for pointers
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while high >= low:

            mid = low + high -low //2

            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[high] and target < nums[mid]:
                low = mid + 1
            else:

                high = mid - 1
        return -1                
        