"""  
Kth Missing Positive Number

Description:
Given a sorted array of positive integers and an integer k,
find the kth missing positive number.

Example:
    Input: arr = [2,3,4,7,11], k = 5
    Output: 9
    Explanation: Missing numbers are [1,5,6,8,9,10,...]. The 5th missing is 9.

Approach:
1. Use binary search to find the boundary position
2. Key insight: At index i, the number of missing positive integers is:
   arr[i] - (i + 1)
   (expected value at index i is i+1, difference gives missing count)
3. Binary search to narrow down where the kth missing number falls
   - If missing_count < k at mid, we need to look further right
   - If missing_count >= k at mid, the kth missing is before arr[mid]
4. After loop exits: left = number of array elements before the kth missing number
5. The kth missing number is: left + k
   (left accounts for array positions, k accounts for missing count)

Time Complexity: O(log n) - Binary search to find position with k missing numbers
Space Complexity: O(1) - Only using constant extra space for pointers
"""

from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left = 0
        right = len(arr) - 1

        while left <= right :

            mid = (left + right ) // 2

            if arr[mid] - (mid + 1) < k:
                left = mid + 1
            else:
                right = mid - 1
        return left + k


"""
Pseudocode (English):
--------------------
1. Start with two pointers: left at beginning (0) and right at end (last index)

2. Key insight: At any index i, count of missing numbers = arr[i] - (i + 1)
   - Example: At index 2, we expect value 3, but if arr[2]=7, missing = 7-3 = 4 numbers

3. While the search space is valid (left hasn't crossed right):
   a. Find the middle element between left and right
   b. Calculate how many numbers are missing up to this middle position
      missing_count = arr[mid] - (mid + 1)
   c. If missing_count is less than k:
      - We need more missing numbers
      - The kth missing number is somewhere to the right
      - Move left pointer to one position after middle
   d. If missing_count is greater than or equal to k:
      - We have enough (or too many) missing numbers
      - Important: Even if missing_count == k, arr[mid] itself is NOT missing
      - The kth missing number is somewhere before arr[mid]
      - We need to narrow down to find the exact position
      - Move right pointer to one position before middle

4. When loop ends (left > right):
   - Left pointer is at the position where we'd have k missing numbers
   - Right pointer is at an index with fewer than k missing numbers
   - The kth missing number = left + k
   - Return left + k

Example walkthrough: arr = [2,3,4,7,11], k = 5
- At index 3: arr[3]=7, missing = 7-4 = 3 (< 5, search right)
- At index 4: arr[4]=11, missing = 11-5 = 6 (>= 5, search left)
- Loop ends with left=4, right=3
- Answer = 4 + 5 = 9 ✓
- Missing numbers before 9: [1,5,6,8,9] - the 5th one is 9
"""