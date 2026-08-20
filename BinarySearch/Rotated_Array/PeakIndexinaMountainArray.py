"""
Peak Index in a Mountain Array

Description:
Given a mountain array (array that increases then decreases), find the index of the peak element.
A mountain array has arr[0] < arr[1] < ... < arr[i-1] < arr[i] > arr[i+1] > ... > arr[n-1].

Example:
    Input: arr = [0,1,0]
    Output: 1
    
    Input: arr = [0,2,1,0]
    Output: 1

Approach:
1. Use binary search to find the peak
2. At each mid point, compare arr[mid] with arr[mid+1]
3. If arr[mid] < arr[mid+1], we're on the ascending side; peak is to the right (left = mid + 1)
4. If arr[mid] > arr[mid+1], we're on the descending side; peak is at mid or to the left (right = mid)
5. When left == right, we've found the peak index
6. Works because there's exactly one peak in a mountain array

Time Complexity: O(log n) - Binary search on the array
Space Complexity: O(1) - Only using constant extra space for pointers
"""

from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        left = 0
        right = len(arr) - 1

        while left < right:

            mid = (left + right) // 2

            if arr[mid] < arr[mid+1]:
                left = mid + 1
            else:
                right = mid

        return left


"""
Pseudocode:
-----------
function peakIndexInMountainArray(arr):
    left = 0
    right = length(arr) - 1
    
    while left < right:
        mid = (left + right) / 2
        
        if arr[mid] < arr[mid + 1]:
            left = mid + 1  // Peak is on right (ascending)
        else:
            right = mid     // Peak is at mid or left (descending)
    
    return left  // Peak index
"""