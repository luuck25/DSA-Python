# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Remove duplicates from a sorted linked list (keep one of each).

        How it works:
        -------------
        Example: 1 -> 1 -> 2 -> 3 -> 3

        Since the list is sorted, duplicates are always adjacent.
        Just compare curr.val with curr.next.val:

        Step 1:  [1] -> [1] -> [2] -> [3] -> [3]
                  ^curr
                  curr.val == curr.next.val → skip: curr.next = curr.next.next

        Step 2:  [1] -> [2] -> [3] -> [3]
                  ^curr
                  curr.val != curr.next.val → move: curr = curr.next

        Step 3:  [1] -> [2] -> [3] -> [3]
                          ^curr
                  curr.val != curr.next.val → move: curr = curr.next

        Step 4:  [1] -> [2] -> [3] -> [3]
                                 ^curr
                  curr.val == curr.next.val → skip: curr.next = curr.next.next

        Result:  [1] -> [2] -> [3] -> None

        No dummy needed — head never changes (we keep the first occurrence).

        Time: O(n) | Space: O(1)
        """
        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next  # skip the duplicate
            else:
                curr = curr.next            # move forward

        return head
