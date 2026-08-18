"""  
First Bad Version

Description:
You are given n versions [1, 2, ..., n] and an API isBadVersion(version) which returns
whether a version is bad. Find the first bad version that caused all following versions to be bad.
Minimize the number of calls to the API.

Example:
    Input: n = 5, bad = 4
    Output: 4
    Explanation: isBadVersion(3) -> false, isBadVersion(4) -> true

Approach:
1. Use binary search between version 1 and n
2. At each iteration, check the middle version using isBadVersion(mid)
3. If mid is a bad version, the first bad version is at mid or earlier
   Search left half (right = mid - 1)
4. If mid is a good version, first bad version is after mid
   Search right half (left = mid + 1)
5. When search completes, left points to the first bad version
6. This minimizes API calls by using binary search instead of linear scan

Time Complexity: O(log n) - Binary search to find the first bad version
Space Complexity: O(1) - Only using constant extra space for pointers
"""

class Solution:
    def firstBadVersion(self, n: int) -> int:

        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2

            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left