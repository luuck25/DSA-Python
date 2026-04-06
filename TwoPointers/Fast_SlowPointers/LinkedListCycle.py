"""
Problem: Linked List Cycle Detection (LeetCode #141)
-----------------------------------------------------
Given the head of a linked list, determine if it has a cycle.

A cycle exists if some node can be reached again by continuously
following the next pointer.

Example:
    Input:  3 -> 2 -> 0 -> -4 -> (back to 2)
    Output: True (cycle exists)
    
    Input:  1 -> 2 -> None
    Output: False (no cycle)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Detect if a linked list has a cycle using Floyd's Algorithm.
        
        Algorithm (Fast and Slow Pointers / Tortoise and Hare):
        -------------------------------------------------------
        Use TWO pointers moving at different speeds:
        - Slow pointer: moves 1 step at a time
        - Fast pointer: moves 2 steps at a time
        
        If there's a cycle, fast pointer will eventually catch up
        to slow pointer (they will meet inside the cycle).
        
        If there's no cycle, fast pointer will reach the end (None).
        
        Visual Example (with cycle):
        ----------------------------
        Initial:  1 -> 2 -> 3 -> 4 -> 5
                  S,F          |     |
                               +--<--+
        
        Step 1:   1 -> 2 -> 3 -> 4 -> 5
                       S    F        |
                               +--<--+
        
        Step 2:   1 -> 2 -> 3 -> 4 -> 5
                            S         F
                               +--<--+
        
        Step 3:   1 -> 2 -> 3 -> 4 -> 5
                            F    S    |
                               +--<--+
        
        Step 4:   S == F -> CYCLE DETECTED!
        
        Why This Works:
        ---------------
        - In a cycle, fast gains 1 step on slow each iteration
        - If cycle length is k, they meet after at most k iterations
        - Like two runners on a circular track - faster one laps slower
        
        Args:
            head: Head node of the linked list
            
        Returns:
            True if cycle exists, False otherwise
            
        Time Complexity: O(n)
            - Without cycle: fast reaches end in n/2 steps
            - With cycle: fast catches slow within cycle length steps
            
        Space Complexity: O(1)
            - Only two pointer variables used
            - No extra data structures needed
        """
        # Edge case: empty list has no cycle
        if head is None:
            return False
        
        # Initialize both pointers at head
        slow_pointer = head
        fast_pointer = head
        
        # Move until fast reaches end (no cycle) or pointers meet (cycle)
        while fast_pointer is not None and fast_pointer.next is not None:
            slow_pointer = slow_pointer.next        # Move 1 step
            fast_pointer = fast_pointer.next.next   # Move 2 steps
            
            # If they meet, cycle exists
            if slow_pointer == fast_pointer:
                return True
        
        # Fast reached end, no cycle
        return False        
        