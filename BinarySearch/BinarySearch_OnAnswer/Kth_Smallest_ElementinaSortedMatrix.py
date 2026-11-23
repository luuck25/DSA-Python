"""
Kth Smallest Element in a Sorted Matrix

Description:
Given an n x n matrix whose rows and columns are sorted in ascending order,
return the kth smallest element.

Approach:
1. Binary search over possible values, starting at the smallest matrix value
    and ending at the largest.
2. For each candidate value `mid`, count how many matrix elements are <= mid.
3. Count efficiently from the bottom-left corner. If the current value is
    <= mid, every value above it in that column is also <= mid, so add
    `row + 1` and move right. Otherwise, move up to a smaller value.
4. If fewer than `k` values are <= mid, the kth smallest value must be larger;
    set `left = mid + 1`.
5. Otherwise, the kth smallest value is at most `mid`; keep the lower half by
    setting `right = mid`.
6. When `left == right`, that value is the kth smallest.

Let:
- `n` = number of rows (and columns)
- `R = largest matrix value - smallest matrix value + 1`

Time Complexity:
1. Set the initial value bounds: O(1).
2. Each binary-search iteration counts values <= mid. The row pointer only
    moves up and the column pointer only moves right; each can move at most n
    times, so one count pass costs O(n).
3. Binary search performs O(log R) iterations because the integer value range
    has R possible values.

    o(n) work in log R itrations so - O(n log R)
Overall: O(n log R).

Space Complexity:
- The algorithm uses a fixed number of indices, bounds, and counters: O(1).
- It does not copy or modify the matrix. The input matrix is not counted as
  extra space.
"""

class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:

        left = matrix[0][0]

        n = len(matrix)

        right = matrix[n-1][n-1]

        while left < right:

            mid = (left + right) // 2
        
            count = 0

            row = n - 1
            col = 0

            while row >=0 and col < n:

                if matrix[row][col] <= mid:

                    count += row + 1
                    col += 1
                else:
                    row -= 1
            if count < k:
                left = mid +1
            else:
                right = mid

        return left


"""
Pseudocode:
-----------
function kthSmallest(matrix, k):
    n = number of rows
    left = smallest matrix value
    right = largest matrix value

    while left < right:
        mid = floor((left + right) / 2)
        count = 0
        row = n - 1
        col = 0

        while row >= 0 and col < n:
            if matrix[row][col] <= mid:
                count += row + 1  // This whole part of the column qualifies
                col += 1
            else:
                row -= 1

        if count < k:
            left = mid + 1  // The kth value is larger
        else:
            right = mid  // The kth value is mid or smaller

    return left
"""






