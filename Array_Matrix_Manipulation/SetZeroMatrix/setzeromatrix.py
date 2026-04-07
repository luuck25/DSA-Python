"""
Set Matrix Zeroes (LeetCode #73)
=================================
Problem:
    If an element is 0, set its entire row and column to 0. In-place.

    Input:  [[1,1,1],     Output: [[1,0,1],
             [1,0,1],              [0,0,0],
             [1,1,1]]              [1,0,1]]

Approach 1 — Brute Force (extra copy):
    Copy matrix, scan original for 0s, zero out rows/cols in copy, copy back.
    Time: O(m×n × (m+n))  Space: O(m×n)

Approach 2 — O(1) Space (use first row/col as markers):
    1. Check if first row or first col originally has a 0 → save flags
    2. Scan rest of matrix: if matrix[r][c] == 0 → mark matrix[r][0] and matrix[0][c]
    3. Use markers to zero out cells (skip first row/col)
    4. Finally, zero out first row/col if flagged

Time:  O(m × n)
Space: O(1)
"""

from typing import List


# ========== Approach 1: Brute Force (extra copy) ==========
class SolutionBrute:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        tmp = [row[:] for row in matrix]  # deep copy

        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    for k in range(col):
                        tmp[i][k] = 0    # zero entire row in copy
                    for k in range(row):
                        tmp[k][j] = 0    # zero entire col in copy

        # copy back to original
        for i in range(row):
            for j in range(col):
                matrix[i][j] = tmp[i][j]


# ========== Approach 2: O(1) Space (first row/col as markers) ==========
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if len(matrix) == 0:
            return

        row = len(matrix)
        col = len(matrix[0])
        firstRowImpacted = False
        firstColImpacted = False

        # Step 1: check if first row has any 0
        for c in range(col):
            if matrix[0][c] == 0:
                firstRowImpacted = True
                break

        # Step 1: check if first col has any 0
        for r in range(row):
            if matrix[r][0] == 0:
                firstColImpacted = True
                break

        # Step 2: use first row/col as markers for rest of matrix
        for r in range(1, row):
            for c in range(1, col):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0  # mark row
                    matrix[0][c] = 0  # mark col

        # Step 3: zero out cells based on markers (skip first row/col)
        for r in range(1, row):
            for c in range(1, col):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # Step 4: handle first row and col using saved flags
        if firstRowImpacted:
            for c in range(col):
                matrix[0][c] = 0

        if firstColImpacted:
            for r in range(row):
                matrix[r][0] = 0

    # ---- Clean version (no comments) ----
    def setZeroes_clean(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return
        row, col = len(matrix), len(matrix[0])
        firstRowImpacted = any(matrix[0][c] == 0 for c in range(col))
        firstColImpacted = any(matrix[r][0] == 0 for r in range(row))

        for r in range(1, row):
            for c in range(1, col):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for r in range(1, row):
            for c in range(1, col):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        if firstRowImpacted:
            for c in range(col):
                matrix[0][c] = 0
        if firstColImpacted:
            for r in range(row):
                matrix[r][0] = 0


                                       