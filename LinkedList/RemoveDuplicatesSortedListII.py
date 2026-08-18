# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Remove ALL nodes that have duplicate values (keep none of them).

        How it works:
        -------------
        Example: 1 -> 2 -> 2 -> 2 -> 3 -> 4 -> 4 -> 5

        Use dummy because head might be a duplicate (e.g., [1,1,2] → [2]).
        prev = last confirmed unique node, curr = node being inspected.

        prev=dummy, curr=node(1)
            1 != 2 → unique → prev=node(1), curr=node(2)

        prev=node(1), curr=node(2)
            2 == 2 → dup! save dup_value=2
            skip ALL nodes with val 2 → curr=node(3)
            prev.next = curr → node(1).next = node(3)

        prev=node(1), curr=node(3)
            3 != 4 → unique → prev=node(3), curr=node(4)

        prev=node(3), curr=node(4)
            4 == 4 → dup! save dup_value=4
            skip ALL nodes with val 4 → curr=node(5)
            prev.next = curr → node(3).next = node(5)

        prev=node(3), curr=node(5)
            5 has no next → unique → prev=node(5), curr=None

        Result: 1 -> 3 -> 5

        Key insight:
          - prev only moves forward on confirmed unique nodes.
          - When a duplicate is found, save the value, skip ALL nodes
            with that value, then connect prev past them.

        Time: O(n) | Space: O(1)
        """
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr:
            if curr.next and curr.val == curr.next.val:
                dup_value = curr.val
                while curr and curr.val == dup_value:
                    curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next

        return dummy.next
