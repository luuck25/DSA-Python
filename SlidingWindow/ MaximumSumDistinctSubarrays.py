"""
Problem: Maximum Sum of Distinct Subarrays with Length K (LeetCode #2461)
-------------------------------------------------------------------------
Find the maximum sum of a subarray of size k where ALL elements are distinct.

If no such subarray exists (all windows have duplicates), return 0.

Example:
    Input:  nums = [1, 5, 4, 2, 9, 9, 9], k = 3
    Output: 15
    Explanation: Subarray [1, 5, 4] and [4, 2, 9] have distinct elements.
                 [4, 2, 9] has max sum = 15
    
    Input:  nums = [4, 4, 4], k = 3
    Output: 0
    Explanation: No subarray of size 3 has all distinct elements.
"""

from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        """
        Find maximum sum of subarray of size k with all distinct elements.
        
        Algorithm (Sliding Window + HashMap):
        --------------------------------------
        This combines sliding window with frequency tracking:
        1. Use a hashmap to track frequency of elements in current window
        2. If duplicate found, shrink window from left until no duplicates
        3. When window size equals k AND all elements distinct, update max
        
        Key Insight:
        ------------
        - We need BOTH conditions: window size = k AND all distinct
        - Use freq map to detect duplicates in O(1) time
        - Shrink window when duplicates found to maintain distinctness
        
        Visual Example (nums = [1, 5, 4, 2, 9, 9, 9], k = 3):
        -----------------------------------------------------
        
        Step 1: Add 1
                [1, 5, 4, 2, 9, 9, 9]
                [1]
                freq = {1:1}, sum = 1, size = 1
        
        Step 2: Add 5
                [1, 5, 4, 2, 9, 9, 9]
                [1, 5]
                freq = {1:1, 5:1}, sum = 6, size = 2
        
        Step 3: Add 4 -> size = k = 3, all distinct!
                [1, 5, 4, 2, 9, 9, 9]
                [1, 5, 4]
                freq = {1:1, 5:1, 4:1}, sum = 10
                maxSum = 10
                Slide: remove 1, freq = {5:1, 4:1}, sum = 9
        
        Step 4: Add 2 -> size = k = 3, all distinct!
                [1, 5, 4, 2, 9, 9, 9]
                   [5, 4, 2]
                freq = {5:1, 4:1, 2:1}, sum = 11
                maxSum = 11
                Slide: remove 5, sum = 6
        
        Step 5: Add 9 -> size = k = 3, all distinct!
                [1, 5, 4, 2, 9, 9, 9]
                      [4, 2, 9]
                freq = {4:1, 2:1, 9:1}, sum = 15
                maxSum = 15
                Slide: remove 4, sum = 11
        
        Step 6: Add 9 -> DUPLICATE! freq[9] = 2
                Shrink until no duplicate:
                Remove 2: freq = {2:0, 9:2}, sum = 9
                Remove 9: freq = {9:1}, sum = 0 (first 9 removed)
                Now window = [9] only, size = 1
        
        Step 7: Add 9 -> DUPLICATE again!
                Shrink: window = [9], size = 1
        
        Final Answer: 15
        
        Args:
            nums: List of integers
            k: Required size of subarray
            
        Returns:
            Maximum sum of subarray with size k and all distinct elements
            
        Time Complexity: O(n)
            - Each element is added to window at most once
            - Each element is removed from window at most once
            - Total: O(2n) = O(n)
            
        Space Complexity: O(k)
            - HashMap stores at most k distinct elements
            - In worst case, all k elements in window are unique
        """
        win_start = 0
        current_sum = 0
        max_sum = 0
        freq = {}  # Frequency map to track duplicates

        for win_end in range(len(nums)):
            # Add current element to window
            curr_ele = nums[win_end]
            current_sum += curr_ele
            freq[curr_ele] = freq.get(curr_ele, 0) + 1

            # If duplicate found, shrink window until no duplicates
            while freq[curr_ele] > 1:
                freq[nums[win_start]] -= 1
                current_sum -= nums[win_start]
                win_start += 1

            # Check if window size equals k (and implicitly all distinct)
            if win_end - win_start + 1 == k:
                max_sum = max(current_sum, max_sum)
                
                # Slide window: remove leftmost element
                freq[nums[win_start]] -= 1
                current_sum -= nums[win_start]
                win_start += 1
                
        return max_sum

    def maximumSubarraySum_self(self, nums: List[int], k: int) -> int:
        elements = set()
        left = 0
        result = 0
        curr_sum = 0

        for right in range(len(nums)):
            while nums[right] in elements:
                curr_sum -= nums[left]
                elements.remove(nums[left])
                left += 1

            elements.add(nums[right])

            if len(elements) > k:
                curr_sum -= nums[left]
                elements.remove(nums[left])
                left += 1

            curr_sum += nums[right]

            if len(elements) == k:
                result = max(result, curr_sum)

        return result


# Test the function
sol = Solution()
print(sol.maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3))
# Output: 15

print(sol.maximumSubarraySum([4, 4, 4], 3))
# Output: 0       