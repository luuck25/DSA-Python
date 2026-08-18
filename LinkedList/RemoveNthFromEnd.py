# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Remove the nth node from the end of the list in one pass.

        How it works (two-pointer gap technique):
        ------------------------------------------
        Example: 1 -> 2 -> 3 -> 4 -> 5,  n=2  (remove node 4)

        Step 1: Advance `fast` by n steps to create a gap of n nodes.

            dummy -> [1] -> [2] -> [3] -> [4] -> [5]
              ^              ^
             slow           fast     (gap = 2)

        Step 2: Move both slow and fast together until fast.next is None.
                slow will land on the node BEFORE the target.

            dummy -> [1] -> [2] -> [3] -> [4] -> [5]
                                    ^              ^
                                   slow          fast

        Step 3: Skip the target node.
            slow.next = slow.next.next  →  node(3).next = node(5)

        Result: 1 -> 2 -> 3 -> 5

        Why dummy?
          - If n == length of list, we're removing the head.
            dummy ensures slow has a node before head to work with.

        Why this works:
          - fast is n nodes ahead of slow.
          - When fast reaches the last node, slow is exactly one node
            before the nth-from-end node.

        Two equivalent while-loop styles:
        -----------------------------------
        Style A (used here): range(n) + while fast.next
          fast stops ON the last node.
          for _ in range(n):    → fast=node(2)
          while fast.next:      → fast walks to node(5), stops there
                                  (fast.next is None → stop)

        Style B (also valid):  range(n+1) + while fast
          fast stops PAST the last node (at None).
          for _ in range(n+1):  → fast=node(3)  (one extra step)
          while fast:           → fast walks to None, stops there
                                  (fast is None → stop)

        Both give slow=node(3) — same result, same iterations.
        The extra initial step in Style B compensates for
        the different stopping condition.

        Time: O(n) | Space: O(1)
        """
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        # Move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # Move both until fast reaches the last node
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Skip the target node
        slow.next = slow.next.next

        return dummy.next
