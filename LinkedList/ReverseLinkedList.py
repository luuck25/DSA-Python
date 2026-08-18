# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse a singly linked list iteratively.

        How it works (3-pointer approach):
        -----------------------------------
        prev = None, curr = head

        Step 1:  None <- [1]    [2] -> [3] -> None
                  prev   curr

        Step 2:  None <- [1] <- [2]    [3] -> None
                          prev   curr

        Step 3:  None <- [1] <- [2] <- [3]
                                  prev  curr

        Each iteration:
          1. Save curr.next in nxt (so we don't lose the rest of the list)
          2. Reverse the pointer: curr.next = prev
          3. Advance prev and curr one step forward

        When curr becomes None, prev is the new head.

        Time: O(n) | Space: O(1)
        """
        prev = None
        curr = head
        while  curr :
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt


        return prev