"""
Problem: Middle of the Linked List (LeetCode #876)
---------------------------------------------------
Given the head of a singly linked list, return the middle node.

If there are two middle nodes (even length), return the SECOND middle node.

Example:
    Input:  1 -> 2 -> 3 -> 4 -> 5
    Output: Node with value 3 (middle)
    
    Input:  1 -> 2 -> 3 -> 4 -> 5 -> 6
    Output: Node with value 4 (second middle)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Find the middle node of a linked list using Fast and Slow Pointers.
        
        Algorithm (Fast and Slow Pointers):
        ------------------------------------
        - Slow pointer: moves 1 step at a time
        - Fast pointer: moves 2 steps at a time
        
        When fast reaches the end, slow will be at the middle!
        
        Why? Fast travels 2x the distance of slow.
        When fast has traveled the full length (n), slow has traveled n/2.
        
        Visual Example (Odd length - 5 nodes):
        --------------------------------------
        Initial:  1 -> 2 -> 3 -> 4 -> 5 -> None
                  S,F
        
        Step 1:   1 -> 2 -> 3 -> 4 -> 5 -> None
                       S    F
        
        Step 2:   1 -> 2 -> 3 -> 4 -> 5 -> None
                            S         F
        
        Step 3:   fastNode.next is None -> STOP!
                  Return slowNode (value 3) -> MIDDLE!
        
        Visual Example (Even length - 6 nodes):
        ---------------------------------------
        Initial:  1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
                  S,F
        
        Step 1:   1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
                       S    F
        
        Step 2:   1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
                            S         F
        
        Step 3:   1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
                                 S              F
        
        Step 4:   fastNode is None -> STOP!
                  Return slowNode (value 4) -> SECOND MIDDLE!
        
        Args:
            head: Head node of the linked list
            
        Returns:
            The middle node (or second middle if even length)
            
        Time Complexity: O(n)
            - We traverse half the list with slow pointer
            - Fast pointer reaches end in n/2 iterations
            
        Space Complexity: O(1)
            - Only two pointer variables used
            - No extra data structures needed
        """
        # Edge case: empty list
        if head is None:
            return head
        
        # Initialize both pointers at head
        slow_node = head
        fast_node = head
        
        # Move until fast reaches the end
        while fast_node is not None and fast_node.next is not None:
            slow_node = slow_node.next        # Move 1 step
            fast_node = fast_node.next.next   # Move 2 steps
        
        # When fast is at end, slow is at middle
        return slow_node    