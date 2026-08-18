# Definition for a Node.
from typing import Optional


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
