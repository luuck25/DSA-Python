# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Reverse nodes from position `left` to `right` (1-indexed) in one pass.

        How it works:
        -------------
        Example: 1 -> 2 -> 3 -> 4 -> 5,  left=2, right=4

        Step 1: Use dummy node and walk to node before `left`:
            dummy -> [1] -> [2] -> [3] -> [4] -> [5]
                      ^
                   prev_left

        Step 2: Reverse (right - left + 1) nodes using 3-pointer technique:
            dummy -> [1]    [4] -> [3] -> [2]    [5]
                      ^      ^(prev)       ^      ^(curr)
                   prev_left          (tail)

        Step 3: Reconnect:
            prev_left.next.next = curr   →  node(2).next = node(5)  (tail -> rest)
            prev_left.next = prev        →  node(1).next = node(4)  (before -> new head)

        Result: 1 -> 4 -> 3 -> 2 -> 5

        Why dummy node?
          - If left=1, the head itself changes. dummy gives a stable anchor
            so we can always return dummy.next as the correct new head.

        Time: O(n) | Space: O(1)
        """
        dummy = ListNode(0, head)
        prev_left = dummy

        # Walk to the node just before position `left`
        for _ in range(left - 1):
            prev_left = prev_left.next

        # Reverse (right - left + 1) nodes
        prev = None
        curr = prev_left.next
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Reconnect: tail of reversed part -> rest, before -> head of reversed part
        prev_left.next.next = curr
        prev_left.next = prev

        return dummy.next


# Alternative Solution (using while loop with counter increment)
class Solution2:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Alternative approach: Uses while loop with left counter increment
        instead of pre-calculating iteration count.
        
        Same logic, different loop style:
        - Checks left <= right condition each iteration
        - Increments left counter as we reverse
        - Includes defensive curr check
        
        Time: O(n) | Space: O(1)
        """
        dummy = ListNode(0, head)
        before_left = dummy

        # Walk to node before position `left`
        for _ in range(left - 1):
            before_left = before_left.next
            
        curr = before_left.next
        prev = None

        # Reverse nodes while left <= right
        while left <= right and curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            left += 1

        # Reconnect the reversed portion
        before_left.next.next = curr
        before_left.next = prev

        return dummy.next
