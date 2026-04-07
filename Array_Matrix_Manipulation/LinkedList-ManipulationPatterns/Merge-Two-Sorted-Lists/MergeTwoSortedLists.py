"""
Merge Two Sorted Lists (LeetCode #21)
======================================
Problem:
    Merge two sorted linked lists into one sorted list (in-place, no new nodes).

    Input:  1→2→4,  1→3→4  →  1→1→2→3→4→4

Logic:
    Dummy head + current pointer.
    Compare heads of both lists — attach the smaller one, advance that list.
    When one list is exhausted, attach the remaining other list.

Time:  O(n + m)
Space: O(1)
"""

from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()                         # dummy head avoids edge-case checks
        curr = dummy

        while list1 is not None and list2 is not None:
            if list1.val > list2.val:
                curr.next = list2                  # list2 is smaller — attach it
                list2 = list2.next
            else:
                curr.next = list1                  # list1 is smaller or equal — attach it
                list1 = list1.next
            curr = curr.next                       # advance build pointer

        if list1 is not None:                      # attach whatever remains
            curr.next = list1
        if list2 is not None:
            curr.next = list2

        return dummy.next                          # skip dummy, return real head

    # ---- Clean version (no comments) ----
    def mergeTwoLists_clean(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        while list1 is not None and list2 is not None:
            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            curr = curr.next

        if list1 is not None:
            curr.next = list1
        if list2 is not None:
            curr.next = list2

        return dummy.next