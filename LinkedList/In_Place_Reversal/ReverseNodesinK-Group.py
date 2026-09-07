# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
PROBLEM: Reverse Nodes in k-Group
Given the head of a linked list, reverse the nodes of the list k at a time,
and return the modified list.

Rules:
- Reverse only complete groups of size k.
- If the remaining nodes are fewer than k, leave them as they are.

APPROACH:
1. Use a dummy node so head updates are easy after reversing the first group.
2. Keep groupPrev as the node before the current group.
3. Find the kth node from groupPrev using helper findKth(...).
    - If kth does not exist, no full group is left, so stop.
4. Mark groupNext = kth.next (node after group).
5. Reverse nodes from groupPrev.next up to kth using standard pointer reversal.
    - Initialize prev = groupNext, curr = groupPrev.next.
    - Reverse until curr reaches groupNext.
6. Reconnect:
    - groupPrev.next should point to kth (new head of reversed group).
    - Move groupPrev to the old group head (now tail) for next iteration.

PSEUDOCODE:
1. dummy -> head
2. groupPrev = dummy
3. loop forever:
    - kth = findKth(groupPrev, k)
    - if kth is None: break
    - groupNext = kth.next
    - prev = groupNext
    - curr = groupPrev.next
    - while curr != groupNext:
         temp = curr.next
         curr.next = prev
         prev = curr
         curr = temp
    - temp = groupPrev.next
    - groupPrev.next = kth
    - groupPrev = temp
4. return dummy.next

TIME COMPLEXITY: O(n)
- Each node is visited a constant number of times across all groups.

SPACE COMPLEXITY: O(1)
- Only constant extra pointers are used.
"""

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0,head)
        groupPrev = dummy

        while True:

            kth = self.findKth(groupPrev,k)

            if not kth:
                break

            groupNext = kth.next

            # reverse group

            prev =  groupNext
            curr = groupPrev.next

            while curr != groupNext:

                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp

        return dummy.next  

    # find Kth Node
    def findKth(self,curr,k):
    
        while curr and k>0:
            curr = curr.next  
            k -= 1
        return curr    







        