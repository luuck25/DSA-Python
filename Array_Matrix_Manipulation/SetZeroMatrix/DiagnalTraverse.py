"""
Diagonal Traverse (LeetCode #498)
===================================
Problem:
    Traverse an m×n matrix in diagonal zigzag order.

    Input:  [[1,2,3],     Output: [1, 2, 4, 7, 5, 3, 6, 8, 9]
             [4,5,6],
             [7,8,9]]

Logic:
    Toggle between going UP-RIGHT and DOWN-LEFT.
    When going up: row--, col++. When going down: row++, col--.
    At boundaries, flip direction:
      Going UP:   hit right wall (col==n-1) → go down (row++). Hit top (row==0) → go right (col++).
      Going DOWN: hit bottom (row==m-1) → go right (col++). Hit left wall (col==0) → go down (row++).

    ⚠️ Check wall before edge: at top-right corner both col==n-1 and row==0 are true.
       col==n-1 must be checked FIRST → correct move is go down, not right.
       Same logic: at bottom-left, row==m-1 checked before col==0.

Time:  O(m × n)
Space: O(1) — result is required output



better to follow standard order:

if col == n - 1:
elif row == 0:

👉 Why?

At top-right corner, both are true
Correct move should be go down, not right


"""

from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        row, col = 0, 0
        m = len(mat)
        n = len(mat[0])
        up = True
        result = []

        for _ in range(m * n):
            result.append(mat[row][col])

            if up:  # moving ↗ (up-right)
                if col == n - 1:       # hit right wall → go down, flip
                    row += 1
                    up = False
                elif row == 0:         # hit top → go right, flip
                    col += 1
                    up = False
                else:
                    row -= 1           # normal diagonal move ↗
                    col += 1
            else:   # moving ↙ (down-left)
                if row == m - 1:       # hit bottom → go right, flip
                    col += 1
                    up = True
                elif col == 0:         # hit left wall → go down, flip
                    row += 1
                    up = True
                else:
                    row += 1           # normal diagonal move ↙
                    col -= 1

        return result

    # ---- Clean version (no comments) ----
    def findDiagonalOrder_clean(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        row, col = 0, 0
        m, n = len(mat), len(mat[0])
        up = True
        result = []

        for _ in range(m * n):
            result.append(mat[row][col])
            if up:
                if col == n - 1:
                    row += 1
                    up = False
                elif row == 0:
                    col += 1
                    up = False
                else:
                    row -= 1
                    col += 1
            else:
                if row == m - 1:
                    col += 1
                    up = True
                elif col == 0:
                    row += 1
                    up = True
                else:
                    row += 1
                    col -= 1
        return result