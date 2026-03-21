"""
Reverse Level Order Traversal (LeetCode #107 variant)
======================================================

Problem:
    Given the root of a binary tree, return the reverse level order traversal 
    of its nodes' values (i.e., from bottom to top, level by level).

Multiple Approaches:
====================

Approach 1: Level Order + Reverse at End
    - Do standard level order traversal (LeetCode #102)
    - Reverse the result list at the end
    - Time: O(n), Space: O(n)
    
    result = level_order_traversal(root)  # [[3], [9,20], [15,7]]
    return result[::-1]                    # [[15,7], [9,20], [3]]

Approach 2: Insert at Position 0 (List)
    - Same as level order, but insert each level at index 0
    - result.insert(0, curr_level)
    - ⚠️ Inefficient! insert(0, x) is O(n) for lists
    - Time: O(n²), Space: O(n)

Approach 3: Use Deque for Result (Current Approach) ✓
    - Same logic as level order traversal
    - Use deque instead of list for result
    - appendleft() is O(1) - efficient insertion at front!
    - Time: O(n), Space: O(n)

Current Implementation Details:
    - Uses deque for BOTH queue (BFS) and result
    - Processes RIGHT child before LEFT (so left appears first when reversed)
    - appendleft() adds each node value to front of result
    
    Note: This gives node-by-node reverse, not level-by-level grouping.
    For grouped output like [[15,7], [9,20], [3]], use Approach 1.

Visual Example:
        3
       / \\
      9   20
         /  \\
        15   7

    Processing Order:
    1. Process 3 → result = [3]
    2. Add right(20), left(9) to queue
    3. Process 20 → result = [20, 3]
    4. Add right(7), left(15) to queue  
    5. Process 9 → result = [9, 20, 3]
    6. Process 7 → result = [7, 9, 20, 3]
    7. Process 15 → result = [15, 7, 9, 20, 3]
    
    Final: [15, 7, 9, 20, 3] (bottom-up, left-to-right)

Why RIGHT before LEFT?
    Since we're adding to front (appendleft), order gets reversed.
    Adding right first → left ends up before right in final result.

Time Complexity: O(n)
    - Each node visited exactly once
    - appendleft() is O(1) for deque

Space Complexity: O(n)
    - Queue holds at most O(w) nodes (w = max width)
    - Result stores all n node values
    - Overall: O(n)
"""

from collections import deque


class Solution:
    def reverseLevelOrder(self, root):
        if root is None:
            return []

        queue = deque([root])   # BFS queue
        result = deque()        # Use deque for O(1) appendleft

        while queue:
            node = queue.popleft()
            result.appendleft(node.val)  # Add to FRONT (reverse effect)

            # Add RIGHT before LEFT (so left appears first after reversal)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

        return list(result)
