"""  
Search a 2D Matrix

Description:
Given an m x n matrix where each row is sorted and the first integer of each row
is greater than the last integer of the previous row, determine if a target value exists.

Example:
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
    Output: True

Approach:
1. Treat the 2D matrix as a flattened 1D sorted array
2. Use binary search on indices from 0 to (m*n - 1)
3. Convert 1D index to 2D coordinates:
   - row = mid // n (number of columns)
   - col = mid % n (remainder gives column position)
4. Compare matrix[row][col] with target and adjust search range
5. Return True if found, False otherwise

Time Complexity: O(log(m*n)) - Binary search treating 2D matrix as 1D sorted array
Space Complexity: O(1) - Only using constant extra space for pointers
"""

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m,n = len(matrix), len(matrix[0])
        left = 0
        right = m * n - 1

        while left <= right:
            mid = (left + right) // 2

            row =  mid // n
            col = mid % n

            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1    

        return False


"""
Pseudocode:
-----------
function searchMatrix(matrix, target):
    m = number of rows
    n = number of columns
    left = 0
    right = m * n - 1
    
    while left <= right:
        mid = (left + right) / 2
        
        // Convert 1D index to 2D coordinates
        row = mid / n
        col = mid % n
        
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False
"""