"""
Transpose Matrix (LeetCode #867)
=================================
Problem:
    Flip a matrix over its main diagonal — rows become columns.

    Input:  [[1,2,3],    Output: [[1,4],
             [4,5,6]]             [2,5],
                                  [3,6]]

Logic (general — any m×n):
    Create new matrix with swapped dimensions (col × row).
    Copy: res[j][i] = matrix[i][j]

Logic (square — n×n, in-place):
    Swap matrix[i][j] with matrix[j][i].
    Only iterate upper triangle (j starts at i+1) to avoid swapping twice.

Time:  O(m × n)
Space: O(m × n) for general, O(1) for in-place square
"""

from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])

        res = [[0] * row for _ in range(col)]  # new matrix: col × row

        for i in range(row):
            for j in range(col):
                res[j][i] = matrix[i][j]  # flip row↔col

        return res


# Square matrix only — in-place swap across diagonal
def transposeInPlace(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):  # upper triangle only — avoids double swap
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


# ---- Clean versions (no comments) ----
def transpose_clean(matrix):
    row, col = len(matrix), len(matrix[0])
    res = [[0] * row for _ in range(col)]
    for i in range(row):
        for j in range(col):
            res[j][i] = matrix[i][j]
    return res


def transposeInPlace_clean(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
