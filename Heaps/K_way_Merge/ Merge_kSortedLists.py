"""
Merge K Sorted Lists

Description:
Given `k` sorted linked lists, merge them into one sorted linked list.

Approach:
1. Put the head node of every nonempty list into a min-heap. Store each entry
    as (node value, unique order, node).
2. The heap gives the smallest currently available node across all lists.
    Pop it and attach that existing node to the merged list.
3. If the popped node has a next node, push that next node into the heap. This
    keeps the heap holding at most one unmerged candidate from each list.
4. Repeat until the heap is empty, then terminate the merged list with None.
5. The unique order value breaks ties between equal node values, so Python
    does not need to compare the linked-list node objects.

Let:
- `k` = number of input lists
- `N` = total number of nodes across all lists

Time Complexity:
1. Add up to k list heads to the heap. Each push costs O(log k),
    so initialization takes O(k log k).
2. Process all N nodes. Each node is popped once and, except for the last node
    in its list, pushed once. Each heap operation costs O(log k),
    so this step takes O(N log k).
3. Attaching nodes and checking their next pointers costs O(N), which is
    included in the heap-operation bound.
Overall: O((N + k) log k). If every list is nonempty, then N >= k, so this
simplifies to O(N log k). For k = 1, heap operations cost O(1), so the total
time is O(N).

Space Complexity:
- The heap holds at most one candidate per input list: O(k).
- The merged list reuses the input nodes, so no separate list of N nodes is
  allocated. Aside from the heap, only a fixed number of pointers and the
  tie-breaking counter are used: O(1) auxiliary space.
Total auxiliary space: O(k). The input nodes are not counted as additional
storage.
"""

import heapq
from itertools import count


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:

        heap = []

        order = count()

        for node in lists:
            if node:
                heapq.heappush(heap,(node.val,next(order),node))


        dummy = ListNode(0)
        tail = dummy

        while heap:

            val,ord, node = heapq.heappop(heap)

            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(heap,(node.next.val,next(order),node.next))  

        tail.next = None

        return dummy.next


"""
Pseudocode:
-----------
function mergeKLists(lists):
    heap = empty min-heap
    order = increasing unique counter

    for each list head in lists:
        if head is not empty:
            push (head.value, next unique order, head) into heap

    dummy = new sentinel node
    tail = dummy

    while heap is not empty:
        value, order, node = pop smallest entry
        append node to the merged list

        if node has a next node:
            push (next node's value, next unique order, next node) into heap

    set tail.next to None
    return dummy.next
"""
        