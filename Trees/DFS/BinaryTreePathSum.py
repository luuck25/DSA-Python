"""
Path Sum (LeetCode #112)
========================

Problem:
    Given the root of a binary tree and an integer targetSum, return True if 
    the tree has a root-to-leaf path such that adding up all the values along 
    the path equals targetSum. A leaf is a node with no children.

Algorithm: DFS with Subtraction (Top-Down Recursion)
    Instead of tracking sum from root, we SUBTRACT current node's value 
    from targetSum and check if remaining equals 0 at a leaf.
    
    1. Base case 1: If node is None → return False (no path)
    2. Base case 2: If leaf AND remaining sum == node.val → return True (found!)
    3. Recursive: Try left subtree OR right subtree with reduced target

Visual Example:
            5
           / \\
          4   8
         /   / \\
        11  13  4
       /  \\      \\
      7    2      1
    
    targetSum = 22
    
    Path: 5 → 4 → 11 → 2
    
    DFS Trace:
    hasPathSum(5, 22)
        → hasPathSum(4, 22-5=17)
            → hasPathSum(11, 17-4=13)
                → hasPathSum(7, 13-11=2)
                    → 7 is leaf, but 7 ≠ 2 → False
                → hasPathSum(2, 13-11=2)
                    → 2 is leaf AND 2 == 2 → True ✓
            → Returns True (short-circuits)
        → Returns True
    
    Answer: True

Why Subtract Instead of Add?
    - Adding approach: Need to pass running sum as extra parameter
    - Subtracting approach: Just modify targetSum, cleaner code
    - Both work! This is a common DFS pattern choice

Why Check "leaf" Condition?
    A path must end at a LEAF (no children), not just any node.
    
    Example:     1
                /
               2
    
    targetSum = 1
    - Node 1 has value 1, but it's NOT a leaf (has left child)
    - We must reach node 2, but 1 + 2 = 3 ≠ 1
    - Answer: False (even though root.val == targetSum)

Short-Circuit Evaluation:
    flag1 or flag2 → If flag1 is True, flag2 is NOT evaluated
    
    Optimization: Can use early return:
        if self.hasPathSum(root.left, targetSum - root.val):
            return True
        return self.hasPathSum(root.right, targetSum - root.val)

Time Complexity: O(n)
    - In worst case, visit every node once
    - n = number of nodes in tree

Space Complexity: O(h) where h = height of tree
    - Recursion stack depth = height of tree
    - Worst case (skewed tree): O(n)
    - Best case (balanced tree): O(log n)
"""

from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Base case: empty node → no path exists
        if root is None:
            return False
        
        # Base case: LEAF node with exact remaining sum → found valid path!
        if root.val == targetSum and root.left is None and root.right is None:
            return True
        
        # Recursive case: try left and right subtrees with reduced target
        # Subtract current node's value from remaining sum
        flag1 = self.hasPathSum(root.left, targetSum - root.val)
        flag2 = self.hasPathSum(root.right, targetSum - root.val)
        
        # Return True if ANY path (left OR right) leads to valid sum
        return flag1 or flag2