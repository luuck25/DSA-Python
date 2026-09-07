"""
PROBLEM: Merge k Sorted Linked Lists
Given an array of k sorted linked lists, merge all the lists into one sorted
linked list and return its head.

APPROACH (Pairwise Merging / Divide-and-Conquer Style):
1. If input list array is empty, return None.
2. Repeatedly merge lists in pairs:
    - Merge list 0 with 1, 2 with 3, and so on.
    - If one list is left without a pair, merge it with None (it stays as is).
3. After one full pass, we get a smaller array of merged lists.
4. Continue until only one list remains.
5. Use a helper merge(l1, l2) (same as merge two sorted lists):
    - Use dummy + curr pointer.
    - Compare node values and attach smaller node each step.
    - Append remaining nodes after one list ends.

PSEUDOCODE:
1. function mergeKLists(lists):
2.     if lists is empty: return None
3.     while size of lists > 1:
4.         merged = []
5.         for i from 0 to size-1 with step 2:
6.             l1 = lists[i]
7.             l2 = lists[i+1] if exists else None
8.             merged.append( merge(l1, l2) )
9.         lists = merged
10.    return lists[0]

11. function merge(l1, l2):
12.    dummy = new node
13.    curr = dummy
14.    while l1 and l2:
15.        attach smaller of l1/l2 to curr.next
16.        move attached list pointer
17.        move curr
18.    curr.next = remaining list
19.    return dummy.next

TIME COMPLEXITY: O(N log k)
- N = total number of nodes across all lists
- Each level of pairwise merging touches all N nodes once
- Number of levels is log k

SPACE COMPLEXITY: O(1) auxiliary (excluding input/output references)
- Merge operation uses constant extra pointers
- Pairing structure reuses list references; no node-copy arrays are built
"""

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        while len(lists) > 1:

            merged = []

            for i in range(0, len(lists), 2):

                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None

                merged.append(self.merge(l1, l2))

            lists = merged 

        return lists[0]       

    def merge(self, l1, l2):

        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next

            curr = curr.next

        curr.next = l1 if l1 else l2

        return dummy.next