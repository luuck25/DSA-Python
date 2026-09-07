# Definition for a Node.

# https://www.youtube.com/watch?v=OLgXN2Yg3xQ
from typing import Optional


"""
========================================
SPACE COMPLEXITY NOTE
========================================

When analyzing space complexity in this problem:

OUTPUT SPACE vs AUXILIARY SPACE:
---------------------------------
- OUTPUT space: The n nodes we create for the copied list (O(n))
- AUXILIARY space: Extra space used by the algorithm itself

CONVENTION:
-----------
When we say "Space: O(1)" for Solution2, we mean AUXILIARY space only.
We do NOT count the output (the copied list) in space complexity analysis.

Both solutions create n new nodes for the result → O(n) output space
  Solution:  Uses hashmap → O(n) auxiliary space
  Solution2: No hashmap  → O(1) auxiliary space (only a few pointers)

TOTAL SPACE = OUTPUT + AUXILIARY:
  Solution:  O(n) + O(n) = O(n) total
  Solution2: O(n) + O(1) = O(n) total

But we report auxiliary space in complexity analysis:
  Solution:  Space: O(n)
  Solution2: Space: O(1)  ← This is the optimization!
"""


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        """
        Deep copy a linked list where each node has a next AND a random pointer.

        Why is this tricky?
        --------------------
        You can't just copy nodes one by one, because the random pointer
        might point to a node that hasn't been created yet.

        Solution: Two-pass with a hashmap.

        How it works:
        -------------
        Example:
            Original:  [7] -> [13] -> [11]
                        |       |       |
                      random  random  random
                        ↓       ↓       ↓
                      None    [7]     [13]

        Pass 1: Create a copy of each node (val only), store in hashmap.
            old_to_new = {
                node(7):  copy(7),
                node(13): copy(13),
                node(11): copy(11),
            }

        Pass 2: Wire up next and random pointers using the hashmap.
            copy(7).next   = old_to_new[node(13)]  → copy(13)
            copy(7).random = old_to_new[None]       → None

            copy(13).next   = old_to_new[node(11)] → copy(11)
            copy(13).random = old_to_new[node(7)]  → copy(7)

            copy(11).next   = old_to_new[None]     → None
            copy(11).random = old_to_new[node(13)] → copy(13)

        Why hashmap?
          - Maps each original node → its copy.
          - When wiring random pointers, we look up the COPY of whatever
            the original's random points to. O(1) lookup.

        Why old_to_new[None] = None?
          - Handles edge cases where next or random is None
            without extra if-checks.

        Time: O(n) | Space: O(n) for the hashmap
        """
        # Map original nodes to their copies. None maps to None.
        old_to_new = {None: None}

        # Pass 1: Create all copy nodes (val only)
        # Use curr to traverse so we don't lose head — we need it again for Pass 2
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # Pass 2: Wire up next and random pointers
        curr = head
        while curr:
            copy = old_to_new[curr]
            copy.next = old_to_new[curr.next]
            copy.random = old_to_new[curr.random]
            curr = curr.next

        return old_to_new[head]


# Alternative Solution: O(1) Space - Interweaving Technique
class Solution2:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        """
        Deep copy with O(1) extra space using node interweaving.
        
        APPROACH:
        ---------
        Instead of using a hashmap, we interweave copy nodes with original nodes
        in the SAME list, then separate them.
        
        Three passes:
        
        PASS 1: Create copy nodes and insert them right after originals
        ----------------------------------------------------------------
        Original:  [7] → [13] → [11] → None
        
        After:     [7] → [7'] → [13] → [13'] → [11] → [11'] → None
                    ↑     ↑      ↑      ↑       ↑      ↑
                  orig  copy   orig   copy    orig   copy
        
        Pattern: original.next = copy
                 copy.next = original.next (old next)
        
        PASS 2: Set random pointers for copy nodes
        -------------------------------------------
        For each original node:
          - Its copy is at original.next
          - If original.random exists, the copy's random should point to
            original.random.next (because that's the COPY of random)
        
        Example:
          original(7).random = None
          copy(7).random = None  ✓
          
          original(13).random = original(7)
          copy(13).random = original(7).next = copy(7)  ✓
        
        PASS 3: Separate the two lists
        -------------------------------
        Restore original list and extract copy list.
        
        [7] → [7'] → [13] → [13'] → [11] → [11'] → None
        
        Split into:
          Original: [7] → [13] → [11] → None
          Copy:     [7'] → [13'] → [11'] → None
        
        WHY O(1) SPACE:
        ---------------
        - No hashmap needed
        - We temporarily modify the original list structure
        - Only use a few pointers (curr, copy, newHead)
        
        Time: O(n) - three passes through the list
        Space: O(1) - no extra data structures (not counting output)
        """
        if not head:
            return None
        
        # PASS 1: Create and interweave copy nodes
        curr = head
        while curr:
            copy = Node(curr.val)
            copy.next = curr.next  # Copy points to original's next
            curr.next = copy       # Original points to copy
            curr = copy.next       # Move to next original node
        
        # PASS 2: Set random pointers for copy nodes
        curr = head
        while curr:
            copy = curr.next
            if curr.random:
                copy.random = curr.random.next  # Random's copy
            curr = copy.next  # Move to next original node
        
        # PASS 3: Separate the lists
        curr = head
        newHead = curr.next  # Head of copied list
        
        while curr:
            copy = curr.next
            curr.next = copy.next  # Restore original list
            
            if copy.next:
                copy.next = copy.next.next  # Link copy to next copy
            
            curr = curr.next  # Move to next original node
        
        return newHead


"""
========================================
COMPARISON: HASHMAP vs INTERWEAVING
========================================

HASHMAP APPROACH (Solution):
  ✓ Easier to understand and implement
  ✓ Clean separation - doesn't modify original
  ✗ O(n) space for hashmap
  
INTERWEAVING APPROACH (Solution2):
  ✓ O(1) extra space
  ✓ Clever use of existing structure
  ✗ More complex logic
  ✗ Temporarily modifies original (restored at end)

VISUAL COMPARISON:
------------------
Hashmap:
  old_to_new = {node(7): copy(7), node(13): copy(13), ...}
  Two separate lists throughout

Interweaving:
  [7] → [7'] → [13] → [13'] → [11] → [11']
  Temporarily merged, then separated

WHEN TO USE WHICH:
------------------
Interview: Explain hashmap first (simpler), then mention O(1) space
           optimization if asked.

Production: Hashmap (more maintainable, space rarely critical for this)

Follow-up: "Can you do it without extra space?" → Use interweaving
"""
