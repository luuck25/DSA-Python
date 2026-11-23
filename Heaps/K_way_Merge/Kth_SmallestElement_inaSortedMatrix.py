"""
Kth Smallest Element in a Sorted Matrix

Description:
Given a row- and column-sorted matrix, return its kth smallest element.

Approach:
1. Put the first element of each row into a min-heap, along with its row and
    column indices. Each row contributes its smallest not-yet-considered value.
2. Pop the heap's smallest entry. Repeating this k times visits matrix values
    in ascending order, so the value popped on the kth iteration is the answer.
3. After popping an entry, push the next value from that same row if one exists.
    This keeps at most one candidate from each row in the heap.

Let:
- `n` = number of rows (and columns, assuming a square matrix)
- `k` = the requested rank

Time Complexity:
1. Add the first value from each of the n rows to the heap. Each push costs
    O(log n), so initialization takes O(n log n).
2. Pop k values. Each pop costs O(log n), for O(k log n) total.
3. After each pop, there may be one push for the next value in that row. There
    are at most k such pushes, costing O(k log n) total.
Overall: O(n log n + k log n), or O((n + k) log n).

Space Complexity:
- The heap holds at most one entry per row: O(n).
- The algorithm uses no separate output collection: O(1) additional variables.
Total extra space: O(n). The input matrix is not counted as extra space.
"""

import heapq


class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:

        heap = []

        for i in range(len(matrix)):
            heapq.heappush(heap,(matrix[i][0],i,0))

        for _ in range(k):

            val, row, col = heapq.heappop(heap)

            if col +1 <  len(matrix):

                heapq.heappush(heap,(matrix[row][col+1],row,col+1))

        return val


"""
Pseudocode:
-----------
function kthSmallest(matrix, k):
    heap = empty min-heap

    for each row index i:
        push (matrix[i][0], i, 0) into heap

    repeat k times:
        value, row, col = pop the smallest entry from heap
        if col + 1 is within this row:
            push (matrix[row][col + 1], row, col + 1) into heap

    return value
"""
            






