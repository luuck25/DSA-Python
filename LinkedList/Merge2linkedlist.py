# Definition for singly-linked list.
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists into one sorted linked list.

        How dummy & curr work:
        -----------------------
        Start:
            dummy -> None
            curr = dummy          (both point to the same node)

        After picking 1 from list1:
            dummy -> [1] -> None
                      ^
                     curr          (curr moved forward)

        After picking 2 from list2:
            dummy -> [1] -> [2] -> None
                             ^
                            curr

        After picking 3 from list1:
            dummy -> [1] -> [2] -> [3] -> None
                                    ^
                                   curr

        dummy nevethe head.
        curr advances each stepr moves — it always points to , building the merged list behind it.
        At the end, dummy.next is the head of the merged list.

        After the loop, one list may still have remaining nodes.
        curr.next = list1 if list1 else list2
          - If list1 still has nodes, append the rest of list1.
          - Otherwise append list2 (which is either the remaining nodes or None).
          - This works because the remaining portion is already sorted
            and its head >= the last merged node, so we just link it directly.

        Time: O(n + m) | Space: O(1)
        """
        dummy = ListNode()
        curr = dummy

        while list1 and list2:

            if list2.val > list1.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        # Attach whichever list still has remaining nodes (or None if both exhausted)
        curr.next = list1 if list1 else list2

        return dummy.next         