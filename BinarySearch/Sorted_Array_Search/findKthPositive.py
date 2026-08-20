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
1. Use binary search to find the insertion point
2. Key insight: At index i, the number of missing positive integers is:
   arr[i] - (i + 1)
   (expected value at index i is i+1, difference gives missing count)
3. Binary search to find the largest index where missing_count < k
4. If arr[mid] - (mid + 1) < k, search right (left = mid + 1)
5. Otherwise, search left (right = mid - 1)
6. After loop, the kth missing number is: left + k

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
Pseudocode:
-----------
function findKthPositive(arr, k):
    left = 0
    right = length(arr) - 1
    
    while left <= right:
        mid = (left + right) / 2
        
        // Calculate missing numbers up to index mid
        missing = arr[mid] - (mid + 1)
        
        if missing < k:
            left = mid + 1  // Need more missing numbers
        else:
            right = mid - 1 // Too many missing numbers
    
    return left + k  // The kth missing number
"""