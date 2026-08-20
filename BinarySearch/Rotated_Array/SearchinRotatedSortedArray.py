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
   - We use >= (not >) to handle edge case when left == mid (single element)
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


"""
Pseudocode:
-----------
1. Initialize two pointers:
   - left pointer at start of array
   - right pointer at end of array

2. While left pointer is less than or equal to right pointer:
   
   a. Calculate middle index between left and right
   
   b. IF element at middle equals target:
      - Return middle index (found!)
   
   c. Determine which half of array is properly sorted:
      
      WHY? Binary search ONLY works on sorted arrays. We must identify which 
      half is sorted so we can use binary search logic (range checking) on it.
      
      IF element at middle >= element at left:
         - Left half is sorted (properly ordered)
         - Note: We use >= (not >) to handle edge case when left == mid
           (When search space is small and mid points to same index as left,
            that single element is trivially sorted)
         
         IF target is within left half's range (between left and middle):
            - We can safely conclude target is in sorted left half
            - Search the sorted left half: move right pointer to middle - 1
         ELSE:
            - Target not in sorted left half (we checked the range)
            - Search the right half: move left pointer to middle + 1
            - Note: We don't search "unsorted" data directly!
            - On next iteration, we'll re-check which half is sorted in the new range
      
      ELSE:
         - Right half is sorted (properly ordered)
         - Left half contains the rotation point
         
         IF target is within right half's range (between middle and right):
            - We can safely conclude target is in sorted right half
            - Search the sorted right half: move left pointer to middle + 1
         ELSE:
            - Target not in sorted right half (we checked the range)
            - Search the left half: move right pointer to middle - 1
            - Note: On next iteration, we'll re-check which half is sorted

3. IF loop exits without finding target:
   - Return -1 (target not found in array)

Key Insights:
-------------
WHY identify the sorted half?
  - Binary search comparisons (less than, greater than) ONLY work on sorted data
  - Range checking (is X between A and B?) only makes sense when sorted
  - In rotated array, at least ONE half is ALWAYS sorted

WHY we never actually "search unsorted" data?
  - We narrow the search space, then RE-EVALUATE on next iteration
  - Each iteration determines which NEW half is sorted
  - Example: [4,5,6,7,0,1,2] → eliminate left [4,5,6,7] → new space [0,1,2] IS sorted!
  - We iteratively find sorted portions until we find target

How it works:
  - Iteration 1: Check which half is sorted, decide direction
  - Iteration 2: In the NEW smaller range, check which half is sorted again
  - Iteration 3: Continue narrowing...
  - We ALWAYS work with sorted portions, just in different iterations
"""