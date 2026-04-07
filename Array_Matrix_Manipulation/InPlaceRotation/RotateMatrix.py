"""
Rotate Image (LeetCode #48)
=============================
Problem:
    Rotate an n×n matrix 90° clockwise, in-place.

    Input:  [[1,2,3],     Output: [[7,4,1],
             [4,5,6],              [8,5,2],
             [7,8,9]]              [9,6,3]]

Logic:
    Rotate layer by layer, outside → inside.
    For each layer, do a 4-way swap moving elements in a cycle:
      topLeft → save temp
      bottomLeft → topLeft
      bottomRight → bottomLeft
      topRight → bottomRight
      temp → topRight

    Each layer shrinks inward (left++, right--) until we reach the center.

Time:  O(n²) — touch every element once
Space: O(1) — only one temp variable

https://www.youtube.com/watch?v=fMSJSS7eO1w
"""

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left, right = 0, len(matrix) - 1

        while right > left:  # process each layer
            for i in range(right - left):  # i offsets within the layer
                top, bottom = left, right

                topLeft = matrix[top][left + i]  # save top-left

                # move bottom-left → top-left
                matrix[top][left + i] = matrix[bottom - i][left]
                # move bottom-right → bottom-left
                matrix[bottom - i][left] = matrix[bottom][right - i]
                # move top-right → bottom-right
                matrix[bottom][right - i] = matrix[top + i][right]
                # move saved top-left → top-right
                matrix[top + i][right] = topLeft

            right -= 1  # shrink layer inward
            left += 1

    # ---- Clean version (no comments) ----
    def rotate_clean(self, matrix: List[List[int]]) -> None:
        left, right = 0, len(matrix) - 1
        while right > left:
            for i in range(right - left):
                top, bottom = left, right
                topLeft = matrix[top][left + i]
                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] = topLeft
            right -= 1
            left += 1


"""
=== DETAILED VISUAL EXPLANATION ===

The Idea: Rotate layer by layer, outside → inside
---------------------------------------------------
For a 4×4 matrix, there are 2 layers:

Layer 0 (outer):          Layer 1 (inner):
[ 1  2  3  4]
[ 5        8]               [ 6  7]
[ 9       12]               [10 11]
[13 14 15 16]

How one layer works — 4-way cycle swap:
----------------------------------------
For each position i in a layer, 4 elements rotate in a cycle:

i = 0:  1 → 4 → 16 → 13 → 1

    Save temp = 1  (topLeft)
    topLeft     = 13  (bottomLeft)
    bottomLeft  = 16  (bottomRight)
    bottomRight = 4   (topRight)
    topRight    = 1   (temp)

i = 1:  2 → 8 → 15 → 9 → 2
i = 2:  3 → 12 → 14 → 5 → 3

That completes the outer layer. Then left++, right-- shrinks inward.

Why top = left and bottom = right?
-----------------------------------
Square matrix — layer boundaries are same for rows and cols:
    Layer 0: left=0, right=3  →  top=0, bottom=3
    Layer 1: left=1, right=2  →  top=1, bottom=2

Why range(right - left) not range(right - left + 1)?
-----------------------------------------------------
Each layer of size n has n-1 swaps (corners are shared):
    Top edge: [1, 2, 3, 4]
               ↑  ↑  ↑  ✗  ← 4 is handled by the right edge
               3 swaps for 4-element layer

The 4 swap lines mapped to directions:
----------------------------------------
    topLeft = matrix[top][left + i]                     # save ↖
    matrix[top][left + i]     = matrix[bottom - i][left]    # ↙ → ↖
    matrix[bottom - i][left]  = matrix[bottom][right - i]   # ↘ → ↙
    matrix[bottom][right - i] = matrix[top + i][right]      # ↗ → ↘
    matrix[top + i][right]    = topLeft                      # ↖ → ↗ (saved)

Assignments go counter-clockwise so values end up clockwise.
"""