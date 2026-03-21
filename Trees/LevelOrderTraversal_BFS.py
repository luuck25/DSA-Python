


"""
Binary Tree Level Order Traversal (LeetCode #102)
==================================================

Problem:
    Given the root of a binary tree, return the level order traversal 
    of its nodes' values (i.e., from left to right, level by level).

Algorithm: Breadth-First Search (BFS) using Queue
    1. Use a queue to process nodes level by level
    2. For each level, process ALL nodes currently in queue
    3. While processing, add children to queue (next level)
    4. Key: len(queue) at start of each iteration = nodes in current level

Visual Example:
        3
       / \\
      9   20
         /  \\
        15   7

    Queue Processing:
    
    Level 0: queue = [3]
             len(queue) = 1 → process 1 node
             Pop 3, add children (9, 20) → queue = [9, 20]
             curr_result = [3]
    
    Level 1: queue = [9, 20]
             len(queue) = 2 → process 2 nodes
             Pop 9, no children
             Pop 20, add children (15, 7) → queue = [15, 7]
             curr_result = [9, 20]
    
    Level 2: queue = [15, 7]
             len(queue) = 2 → process 2 nodes
             Pop 15, no children
             Pop 7, no children → queue = []
             curr_result = [15, 7]
    
    Result: [[3], [9, 20], [15, 7]]

Why use for loop with range(len(qq))?
    - len(qq) is captured BEFORE we start popping
    - This tells us exactly how many nodes are at current level
    - New nodes added (children) won't be processed in this iteration
    
    Without this trick, we'd mix nodes from different levels!

BFS vs DFS for Trees:
    BFS (this solution):
        - Uses Queue (FIFO)
        - Explores level by level (breadth first)
        - Natural fit for level-order traversal
    
    DFS (alternative):
        - Uses Stack or Recursion
        - Explores depth first (goes deep before siblings)
        - Natural fit for preorder/inorder/postorder

Time Complexity: O(n)
    - Each node is visited exactly once
    - n = total number of nodes in the tree

Space Complexity: O(w) where w = maximum width of tree
    - Queue holds at most one level at a time
    - Worst case (complete binary tree): last level has ~n/2 nodes → O(n)
    - Best case (skewed tree): only 1 node per level → O(1)
    - Average/typical: O(n) considering the result storage
"""

import collections
from typing import Optional, List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []  # Final result: list of levels, each level is a list of values

        # Edge case: empty tree
        if root is None:
            return result

        # Initialize queue with root node (BFS uses FIFO queue)
        qq = collections.deque()
        qq.append(root)

        # Process level by level until queue is empty
        while qq:
            curr_result = []  # Store all node values at current level
            
            # CRITICAL: Capture queue length BEFORE processing
            # This is the number of nodes at current level
            level_size = len(qq)
            
            for i in range(level_size):
                # Remove node from front of queue (FIFO)
                node = qq.popleft()
                curr_result.append(node.val)
                
                # Add children to queue (they'll be processed in next level)
                if node.left is not None:
                    qq.append(node.left)
                if node.right is not None:
                    qq.append(node.right)
            
            # Add current level to result
            result.append(curr_result)
        
        return result       





        



        