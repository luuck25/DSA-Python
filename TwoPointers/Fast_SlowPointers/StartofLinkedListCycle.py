"""
Problem: Linked List Cycle II - Find Start of Cycle (LeetCode #142)
--------------------------------------------------------------------
Given the head of a linked list, return the node where the cycle begins.
If there is no cycle, return None.

Example:
    Input:  3 -> 2 -> 0 -> -4
                 ^          |
                 +----<-----+
    Output: Node with value 2 (cycle starts here)
    
    Input:  1 -> 2 -> None
    Output: None (no cycle)
"""

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Find the starting node of a cycle in a linked list.
        
        Algorithm (Floyd's Cycle Detection + Math):
        --------------------------------------------
        Phase 1: Detect if cycle exists (fast and slow pointers)
        Phase 2: Find the start of the cycle
        
        Mathematical Proof:
        -------------------
        Let's define:
        - L = distance from head to cycle start
        - C = cycle length
        - K = distance from cycle start to meeting point
        
        When slow and fast meet:
        - Slow traveled: L + K
        - Fast traveled: L + K + nC (n complete cycles)
        
        Since fast travels 2x slow's speed:
        2(L + K) = L + K + nC
        L + K = nC
        L = nC - K
        L = (n-1)C + (C - K)
        
        This means: distance from HEAD to cycle start (L)
                  = distance from MEETING POINT to cycle start (C - K)
        
        So if we move one pointer from head and another from meeting point
        at the same speed, they will meet at the cycle start!
        
        Visual Example:
        ---------------
        List: 1 -> 2 -> 3 -> 4 -> 5
                   ^              |
                   +------<-------+
        
        L = 1 (head to cycle start, node 2)
        C = 4 (cycle length: 2 -> 3 -> 4 -> 5 -> 2)
        
        Phase 1 - Find meeting point:
        -----------------------------
        Step 0: S=1, F=1
        Step 1: S=2, F=3
        Step 2: S=3, F=5
        Step 3: S=4, F=3 (fast went 5->2->3)
        Step 4: S=5, F=5 -> MEET!
        
        Phase 2 - Find cycle start:
        ---------------------------
        Move one pointer from head, one from meeting point:
        Step 0: ptr1=1, ptr2=5
        Step 1: ptr1=2, ptr2=2 -> MEET at cycle start!
        
        Args:
            head: Head node of the linked list
            
        Returns:
            Node where cycle begins, or None if no cycle
            
        Time Complexity: O(n)
            - Phase 1: O(n) to detect cycle
            - Phase 2: O(n) to find start (at most L steps)
            
        Space Complexity: O(1)
            - Only pointer variables used
            - No extra data structures needed
        """
        # Edge case: empty list
        if head is None:
            return None
        
        slow_node = head
        fast_node = head
        
        # Phase 1: Detect cycle using fast and slow pointers
        while fast_node is not None and fast_node.next is not None:
            slow_node = slow_node.next        # Move 1 step
            fast_node = fast_node.next.next   # Move 2 steps
            
            # Cycle detected - pointers meet
            if slow_node == fast_node:
                # Phase 2: Find the start of the cycle
                # Move one pointer to head, keep other at meeting point
                fast_node = head
                
                # Move both at same speed - they meet at cycle start
                while slow_node is not fast_node:
                    slow_node = slow_node.next
                    fast_node = fast_node.next
                
                return slow_node  # This is the cycle start
        
        # No cycle found
        return None