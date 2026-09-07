# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
========================================
MODULO (%) vs DIVISION (//) - KEY CONCEPT
========================================

Division (//):  "How many complete times does this number fit?"
Modulo (%):     "What's left over?"

EXAMPLE: 17 ÷ 5
---------------
17 = 5 × 3 + 2

17 // 5  →  3  (quotient - how many complete groups)
17 % 5   →  2  (remainder - what's left over)

WHEN NUMBER IS SMALLER THAN DIVISOR:
-------------------------------------
3 = 10 × 0 + 3

3 // 10  →  0  (10 doesn't fit into 3 even once)
3 % 10   →  3  (entire number is left over)

Examples:
  7 // 10 = 0,  7 % 10 = 7
  9 // 10 = 0,  9 % 10 = 9
 13 // 10 = 1, 13 % 10 = 3
 27 // 10 = 2, 27 % 10 = 7

WHY THIS MATTERS FOR ADD TWO NUMBERS:
--------------------------------------
When adding digits, we need:
  - Current digit (ones place) → use % 10
  - Carry (tens place)         → use // 10

Example: total = 17
  digit = 17 % 10   →  7  (current digit)
  carry = 17 // 10  →  1  (carry forward)

Example: total = 7 (no carry needed)
  digit = 7 % 10    →  7  (current digit)
  carry = 7 // 10   →  0  (no carry)

PATTERN FOR EXTRACTING DIGITS:
-------------------------------
123 % 10  → 3   (last digit)
123 // 10 → 12  (remove last digit)

12 % 10   → 2   (last digit)
12 // 10  → 1   (remove last digit)

Memory trick:
  %  → what remains (current digit)
  // → what goes forward (carry)
"""


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Add two numbers represented as reversed linked lists.
        
        PROBLEM:
        --------
        Given two non-empty linked lists representing two non-negative integers,
        where digits are stored in REVERSE order (least significant digit first).
        Add the two numbers and return the sum as a linked list.
        
        Example: 342 + 465 = 807
          l1: [2] → [4] → [3]     (represents 342)
          l2: [5] → [6] → [4]     (represents 465)
          result: [7] → [0] → [8] (represents 807)
        
        APPROACH:
        ---------
        Simulate elementary school addition (right to left):
        1. Add corresponding digits from both lists
        2. Track carry for next position
        3. Handle different list lengths (treat missing as 0)
        4. Continue until both lists exhausted AND no carry remains
        
        Visual trace for [2→4→3] + [5→6→4]:
        
        Step 1: 2 + 5 + 0(carry) = 7, carry=0
          dummy → [7]
        
        Step 2: 4 + 6 + 0(carry) = 10, carry=1, digit=0
          dummy → [7] → [0]
        
        Step 3: 3 + 4 + 1(carry) = 8, carry=0
          dummy → [7] → [0] → [8]
        
        Step 4: No more digits, no carry → done
        
        Edge cases handled:
          - Different lengths: [9,9] + [1] → [0,0,1]
          - Final carry: [5] + [5] → [0,1]
          - All zeros: [0] + [0] → [0]
        
        Time Complexity: O(max(m, n))
          - m = length of l1, n = length of l2
          - Visit each digit once
        
        Space Complexity: O(max(m, n))
          - Result list has at most max(m,n) + 1 nodes
          - Not counting output, O(1) extra space (just carry variable)
        """
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            # Get digit values (0 if list exhausted)
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0

            # Add digits + carry
            total = digit1 + digit2 + carry

            # Create new node with digit (total % 10)
            current.next = ListNode(total % 10)

            # Update carry for next iteration
            carry = total // 10

            # Move to next node in result
            current = current.next

            # Move to next digits in input lists
            if l1:
                l1 = l1.next 
            if l2:
                l2 = l2.next

        return dummy.next


"""
PSEUDOCODE (English):
---------------------
1. Create a dummy node to build the result list
2. Initialize current pointer to dummy
3. Initialize carry to 0

4. WHILE at least one list has digits OR carry exists:
   a. Get digit from l1 (or 0 if l1 is exhausted)
   b. Get digit from l2 (or 0 if l2 is exhausted)
   
   c. Calculate: total = digit1 + digit2 + carry
   
   d. Create new node with value = total % 10 (ones place)
   e. Attach new node to current.next
   
   f. Update carry = total // 10 (tens place)
   
   g. Move current pointer forward
   h. Move l1 forward (if exists)
   i. Move l2 forward (if exists)

5. Return dummy.next (head of result list)

KEY INSIGHTS:
-------------
- Lists are in REVERSE order, so we naturally add from least to most significant
- Using dummy node simplifies head creation
- Loop continues while ANY list has digits OR carry exists
- Treating exhausted lists as 0 handles different lengths elegantly
- Modulo (%) gets the digit, division (//) gets the carry

EXAMPLES:
---------
Example 1: [2,4,3] + [5,6,4] = [7,0,8]
  342 + 465 = 807

Example 2: [9,9,9] + [1] = [0,0,0,1]
  999 + 1 = 1000

Example 3: [0] + [0] = [0]
  0 + 0 = 0
"""            

