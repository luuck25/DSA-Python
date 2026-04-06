"""
Find the Duplicate Number (LeetCode #287)
==========================================
Problem:
    Array of n+1 integers where each is in [1, n]. Exactly one duplicate.
    Find it without modifying array and using O(1) space.

    Input:  [1, 3, 4, 2, 2]  →  2

Logic:
    Treat array as a linked list: index → nums[index] → nums[nums[index]]...
    A duplicate value means two indices point to the same next → cycle exists.
    Use Floyd's Cycle Detection (same as LinkedList cycle):
      Phase 1: slow (1 step) & fast (2 steps) until they meet inside the cycle.
      Phase 2: Reset slow to start, move both 1 step → they meet at cycle entrance = duplicate.

Time:  O(n)
Space: O(1)
"""

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Detect cycle — slow moves 1 step, fast moves 2 steps
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]           # 1 hop
            fast = nums[nums[fast]]     # 2 hops
            if slow == fast:            # they meet inside the cycle
                break
        
        # Phase 2: Find cycle entrance — reset slow to head, both move 1 step
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow  # meeting point = the duplicate number

    # ---- Clean version (no comments) ----
    def findDuplicate_clean(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow