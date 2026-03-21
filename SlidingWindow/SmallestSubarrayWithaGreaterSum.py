"""
Minimum Size Subarray Sum (LeetCode #209)
=========================================

Problem:
    Given an array of positive integers `nums` and a positive integer `target`,
    find the minimal length of a contiguous subarray whose sum is >= target.
    Return 0 if no such subarray exists.

Algorithm: Variable-Size Sliding Window
    Unlike fixed-size sliding window, here the window SHRINKS when condition is met.
    
    1. Expand window by moving wind_end (add elements to sum)
    2. Once sum >= target, SHRINK window from left to find minimum length
    3. Keep shrinking while condition holds (greedy optimization)
    
Visual Example:
    nums = [2, 3, 1, 2, 4, 3], target = 7
    
    Step 1: [2] → sum=2 < 7, expand
    Step 2: [2,3] → sum=5 < 7, expand  
    Step 3: [2,3,1] → sum=6 < 7, expand
    Step 4: [2,3,1,2] → sum=8 >= 7 ✓ length=4, shrink!
            [3,1,2] → sum=6 < 7, stop shrinking
    Step 5: [3,1,2,4] → sum=10 >= 7 ✓ length=4, shrink!
            [1,2,4] → sum=7 >= 7 ✓ length=3, shrink!
            [2,4] → sum=6 < 7, stop shrinking
    Step 6: [2,4,3] → sum=9 >= 7 ✓ length=3, shrink!
            [4,3] → sum=7 >= 7 ✓ length=2 ← minimum found!
            [3] → sum=3 < 7, stop shrinking
    
    Answer: 2 (subarray [4,3])

Key Insight - Why WHILE loop (not IF)?
    When sum >= target, the minimum subarray might be even smaller!
    We keep shrinking until sum drops below target.
    
    Example: nums=[1,1,1,1,100], target=5
    When we reach 100: sum=104 >= 5
    - Shrink: [1,1,1,100] sum=103 >= 5 ✓
    - Shrink: [1,1,100] sum=102 >= 5 ✓
    - Shrink: [1,100] sum=101 >= 5 ✓
    - Shrink: [100] sum=100 >= 5 ✓ length=1 ← optimal!

Time Complexity: O(n)
    - Each element is visited at most twice (once by wind_end, once by wind_start)
    - The inner while loop doesn't make it O(n²) because wind_start 
      moves forward across all iterations (amortized analysis)

Space Complexity: O(1)
    - Only using a few integer variables
"""

from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')  # Track minimum length found (infinity = none found yet)
        wind_start = 0             # Left boundary of sliding window
        current_sum = 0            # Running sum of current window
        
        # Expand window by moving right boundary
        for wind_end in range(len(nums)):
            current_sum += nums[wind_end]  # Add new element to window sum

            # SHRINK window while condition is satisfied (greedy)
            while current_sum >= target:
                # Update minimum length
                min_length = min(min_length, wind_end - wind_start + 1)
                # Remove leftmost element and shrink window
                current_sum -= nums[wind_start]
                wind_start += 1

        # Return 0 if no valid subarray found, else return minimum length
        return 0 if min_length == float('inf') else min_length
