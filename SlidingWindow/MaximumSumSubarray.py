"""
Problem: Maximum Sum Subarray of Size K
----------------------------------------
Given an array of integers and a number k, find the maximum sum
of a contiguous subarray of size k.

This is a classic Sliding Window problem.

Example:
    Input:  arr = [2, 1, 5, 1, 3, 2], k = 3
    Output: 9
    Explanation: Subarray [5, 1, 3] has maximum sum = 9
    
    Input:  arr = [2, 3, 4, 1, 5], k = 2
    Output: 7
    Explanation: Subarray [3, 4] has maximum sum = 7
"""


class Solution:
    def maxSubarraySum(self, arr: list[int], k: int) -> int:
        """
        Find maximum sum of any contiguous subarray of size k.
        
        Algorithm (Sliding Window - Fixed Size):
        -----------------------------------------
        Instead of recalculating sum for each window (O(n*k)),
        we SLIDE the window by:
        1. Adding the new element entering the window
        2. Removing the old element leaving the window
        
        This gives us O(n) time complexity!
        
        Visual Example (arr = [2, 1, 5, 1, 3, 2], k = 3):
        -------------------------------------------------
        
        Step 1: Build first window of size k
                [2, 1, 5, 1, 3, 2]
                [-----]
                sum = 2 + 1 + 5 = 8
                maxSum = 8
        
        Step 2: Slide window right (remove 2, add 1)
                [2, 1, 5, 1, 3, 2]
                   [-----]
                sum = 8 - 2 + 1 = 7
                maxSum = max(8, 7) = 8
        
        Step 3: Slide window right (remove 1, add 3)
                [2, 1, 5, 1, 3, 2]
                      [-----]
                sum = 7 - 1 + 3 = 9
                maxSum = max(8, 9) = 9
        
        Step 4: Slide window right (remove 5, add 2)
                [2, 1, 5, 1, 3, 2]
                         [-----]
                sum = 9 - 5 + 2 = 6
                maxSum = max(9, 6) = 9
        
        Final Answer: 9
        
        Key Insight:
        ------------
        - Window becomes valid when windowEnd >= k - 1
        - At each valid position:
          1. Update maxSum if current window sum is larger
          2. Subtract element leaving the window (arr[windowStart])
          3. Move windowStart forward
        
        Args:
            arr: List of integers
            k: Size of the subarray window
            
        Returns:
            Maximum sum of any contiguous subarray of size k
            
        Time Complexity: O(n)
            - Single pass through the array
            - Each element is added once and removed once
            
        Space Complexity: O(1)
            - Only a few variables used (windowStart, currentSum, maxSum)
            - No extra data structures needed
        """
        window_start = 0
        current_sum = 0
        max_sum = 0

        for window_end in range(len(arr)):
            # Add the next element to the window
            current_sum += arr[window_end]

            # Check if we've reached a valid window size (k elements)
            if window_end >= k - 1:
                # Update max if current window sum is larger
                max_sum = max(current_sum, max_sum)
                
                # Slide the window: remove the leftmost element
                current_sum -= arr[window_start]
                
                # Move window start forward
                window_start += 1
                
        return max_sum


# Test the function
sol = Solution()
print(sol.maxSubarraySum([2, 1, 5, 1, 3, 2], 3))
# Output: 9


print(sol.maxSubarraySum([2, 3, 4, 1, 5], 2))
# Output: 7        
        