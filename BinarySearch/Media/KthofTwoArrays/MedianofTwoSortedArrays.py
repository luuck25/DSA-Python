"""
Median of Two Sorted Arrays

Description:
Given two sorted arrays nums1 and nums2, find the median of the two sorted arrays.
The overall run time complexity must be O(log(min(m,n))).

Example:
    Input: nums1 = [1,3], nums2 = [2]
    Output: 2.0
    Explanation: merged array = [1,2,3], median is 2
    
    Input: nums1 = [1,2], nums2 = [3,4]
    Output: 2.5
    Explanation: merged array = [1,2,3,4], median is (2 + 3) / 2 = 2.5

Approach:
1. Binary search on the smaller array to find the correct partition
2. Ensure nums1 is the smaller array (swap if needed)
3. Binary search on nums1 to find partition point:
   - Why right = m (not m-1)? We're searching partition positions [0 to m], not element indices [0 to m-1]
     * partition = 0: take 0 elements (cut before all)
     * partition = m: take all m elements (cut after all)
   - Why left <= right? We return immediately when valid partition is found (like Template 1)
   - partition1 divides nums1, partition2 divides nums2
   - For median, left half must have (m + n + 1) // 2 elements total
   - Why +1? Handles both even and odd lengths:
     * Even: (4+1)//2 = 2, left=2, right=2 ✓
     * Odd: (5+1)//2 = 3, left=3, right=2 ✓ (extra goes to left for median)
   - partition1 + partition2 = (m + n + 1) // 2
   - Therefore: partition2 = (m + n + 1) // 2 - partition1
4. Check if valid partition: left1 <= right2 AND left2 <= right1
5. If valid:
   - Odd total length: return max(left1, left2)
   - Even total length: return (max(left1, left2) + min(right1, right2)) / 2
6. If left1 > right2, move partition1 left (right = partition1 - 1)
7. If left2 > right1, move partition1 right (left = partition1 + 1)
8. Use infinity/-infinity for edge cases when partition is at boundaries

Time Complexity: O(log(min(m,n))) - Binary search on the smaller array
Space Complexity: O(1) - Only using constant extra space for pointers

https://www.youtube.com/watch?v=7nABqJCEMuY
"""

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1 , nums2 = nums2, nums1

        m =len(nums1)
        n = len(nums2)     

        left = 0
        right = m

        while left <= right:

            partition1 = (left + right) // 2
            partition2  = (m + n +1 )//2 - partition1

            left1 = float('-inf') if partition1 == 0 else nums1[partition1-1]
            right1 = float('inf') if partition1 == m else nums1[partition1]
            left2 =  float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            right2 = float('inf') if partition2 == n else nums2[partition2]

            if left1 <= right2 and left2 <= right1:

                if (m+n) % 2 ==1:
                    return max(left1,left2)
                else:

                    return (max(left1,left2) + min(right1,right2))/2 
            elif left1 > right2:
                right = partition1 - 1
            else:
                left = partition1 + 1               


"""
Pseudocode (English):
--------------------
function findMedianSortedArrays(nums1, nums2):
    // Ensure nums1 is the smaller array
    if length(nums1) > length(nums2):
        swap(nums1, nums2)
    
    m = length(nums1)
    n = length(nums2)
    left = 0
    right = m  // Not m-1! Partition positions range [0, m], not indices [0, m-1]
    
    while left <= right:  // Use <= because we return immediately when found
        partition1 = (left + right) / 2
        partition2 = (m + n + 1) / 2 - partition1  // +1 handles both even/odd
        
        // Get boundary elements (use infinity for edge cases)
        left1 = partition1 == 0 ? -infinity : nums1[partition1 - 1]
        right1 = partition1 == m ? infinity : nums1[partition1]
        left2 = partition2 == 0 ? -infinity : nums2[partition2 - 1]
        right2 = partition2 == n ? infinity : nums2[partition2]
        
        // Check if valid partition
        if left1 <= right2 AND left2 <= right1:
            // Found correct partition
            if (m + n) is odd:
                return max(left1, left2)
            else:
                return (max(left1, left2) + min(right1, right2)) / 2
        
        elif left1 > right2:
            right = partition1 - 1  // Move partition1 left
        else:
            left = partition1 + 1   // Move partition1 right
"""