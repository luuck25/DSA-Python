"""
PROBLEM: Reorder Linked List
Given a singly linked list L0 → L1 → L2 → ... → Ln-1 → Ln,
reorder it to: L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...
You must do this in-place without altering the nodes' values.

APPROACH:
This problem is solved using three main steps:
1. Find the middle of the linked list using slow and fast pointers
2. Reverse the second half of the list
3. Merge the two halves by alternating nodes from first and second half

Step-by-step:
- Use two pointers (slow and fast) to find the middle point
- Split the list into two halves at the middle
- Reverse the second half completely
- Merge both halves by taking one node from first half, then one from second half

PSEUDOCODE:
1. Handle edge cases (empty list or single node)
2. Find middle of list:
   - Initialize slow and fast pointers at head
   - Move slow by 1 step and fast by 2 steps
   - When fast reaches end, slow is at middle
3. Split list into two halves:
   - Second half starts at slow.next
   - Set slow.next = None to separate the lists
4. Reverse second half:
   - Use three pointers: prev, current, temp
   - For each node, reverse the next pointer
   - Continue until entire second half is reversed
5. Merge two halves:
   - Take one node from first half
   - Insert one node from second half after it
   - Repeat until second half is exhausted

TIME COMPLEXITY: O(n)
- Finding middle: O(n/2) = O(n)
- Reversing second half: O(n/2) = O(n)
- Merging: O(n/2) = O(n)
- Total: O(n) where n is the number of nodes

SPACE COMPLEXITY: O(1)
- Only using constant extra space (pointers)
- No additional data structures needed
- In-place modification of the list
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Edge case: empty list or single node
        if not head or not head.next:
            return
        
        # STEP 1: Find the middle of the linked list
        # Using slow and fast pointer technique
        slow = head
        fast = head

        # Fast moves 2x speed, when fast reaches end, slow is at middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # STEP 2: Split the list into two halves
        # Second half starts from slow.next
        second = slow.next
        slow.next = None  # Break the link to split the list
        
        # STEP 3: Reverse the second half of the list
        prev = None

        while second:
            tmp = second.next       # Save next node
            second.next = prev      # Reverse the pointer
            prev = second           # Move prev forward
            second = tmp            # Move to next node

        # After reversal, prev points to the head of reversed second half
        second = prev
        first = head

        # STEP 4: Merge the two halves alternately
        # Pattern: first -> second -> first.next -> second.next -> ...
        while second:
            tmp = second.next       # Save next node from second half
            tmp1 = first.next       # Save next node from first half

            first.next = second     # Link first to second
            second.next = tmp1      # Link second to first.next

            second = tmp            # Move to next in second half
            first = tmp1            # Move to next in first half

  




       
            
            


        