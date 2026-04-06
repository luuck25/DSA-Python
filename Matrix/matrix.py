"""
Matrix Traversal Methods in Python — All Patterns with Examples
================================================================

Sample Matrix (used throughout):
    matrix = [
        [1,  2,  3,  4],
        [5,  6,  7,  8],
        [9,  10, 11, 12],
        [13, 14, 15, 16]
    ]

    Visual:
         col0  col1  col2  col3
    row0 [  1,    2,    3,    4 ]
    row1 [  5,    6,    7,    8 ]
    row2 [  9,   10,   11,   12 ]
    row3 [ 13,   14,   15,   16 ]

          col0      col1      col2      col3
row0   [0][0]=1   [0][1]=2   [0][2]=3   [0][3]=4
row1   [1][0]=5   [1][1]=6   [1][2]=7   [1][3]=8
row2   [2][0]=9   [2][1]=10  [2][2]=11  [2][3]=12
row3   [3][0]=13  [3][1]=14  [3][2]=15  [3][3]=16

    rows = len(matrix)      = 4
    cols = len(matrix[0])   = 4
"""


# ============================================================
# 0. SIMPLEST TRAVERSAL (No indices needed)
# ============================================================
# When you just need every value and DON'T care about position.
# Python lets you loop directly over rows, then values.
#
# Output: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
#
# Use when: counting, summing, finding min/max, checking existence
# DON'T use when: you need row/col index (use row-wise instead)

def traverse_simple(matrix):
    for row in matrix:          # row = [1, 2, 3, 4], then [5, 6, 7, 8], etc.
        for val in row:         # val = each individual number
            print(val, end=" ")
    print()


# ============================================================
# 1. ROW-WISE TRAVERSAL (Left → Right, Top → Bottom)
# ============================================================
# The most basic and common traversal.
# Visit every element row by row.
#
# Output: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16

def traverse_row_wise(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for r in range(rows):
        for c in range(cols):
            print(matrix[r][c], end=" ")
    print()


# ============================================================
# 2. COLUMN-WISE TRAVERSAL (Top → Bottom, Left → Right)
# ============================================================
# Visit every element column by column.
#
# Output: 1 5 9 13 2 6 10 14 3 7 11 15 4 8 12 16

def traverse_col_wise(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for c in range(cols):
        for r in range(rows):
            print(matrix[r][c], end=" ")
    print()


# ============================================================
# 3. DIAGONAL TRAVERSAL (Top-Left → Bottom-Right)
# ============================================================
# Main diagonal: (0,0), (1,1), (2,2), (3,3)
# All diagonals starting from first row and first column.
#
# Output diagonals: [1] [2,5] [3,6,9] [4,7,10,13] [8,11,14] [12,15] [16]

def traverse_diagonal(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Diagonals starting from first row (col 0 to cols-1)
    for start_col in range(cols):
        r, c = 0, start_col
        diag = []
        while r < rows and c < cols:
            diag.append(matrix[r][c])
            r += 1
            c += 1
        print(diag)

    # Diagonals starting from first column (row 1 to rows-1)
    # Start from row 1 to avoid repeating the (0,0) diagonal
    for start_row in range(1, rows):
        r, c = start_row, 0
        diag = []
        while r < rows and c < cols:
            diag.append(matrix[r][c])
            r += 1
            c += 1
        print(diag)


# ============================================================
# 4. ANTI-DIAGONAL TRAVERSAL (Top-Right → Bottom-Left)
# ============================================================
# Anti-diagonals go from top-right to bottom-left.
# Elements on same anti-diagonal have same (row + col) value.
#
# Output: [1] [2,5] [3,6,9] [4,7,10,13] [8,11,14] [12,15] [16]
#   (Same grouping as diagonal for square matrix, diff direction)

def traverse_anti_diagonal(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Group elements by (row + col) — they share the same anti-diagonal
    from collections import defaultdict
    diagonals = defaultdict(list)

    for r in range(rows):
        for c in range(cols):
            diagonals[r + c].append(matrix[r][c])

    for key in sorted(diagonals.keys()):
        print(diagonals[key])


# ============================================================
# 5. SPIRAL TRAVERSAL (Outside → Inside, Clockwise)
# ============================================================
# Go: Right → Down → Left → Up → repeat, shrinking boundaries.
#
# Output: 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
#
# Visual (arrows show direction):
#     → → → →
#     ↑       ↓
#     ↑       ↓
#     ← ← ← ←

def traverse_spiral(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []

    top, bottom = 0, rows - 1
    left, right = 0, cols - 1

    while top <= bottom and left <= right:
        # → Move RIGHT across the top row
        for c in range(left, right + 1):
            result.append(matrix[top][c])
        top += 1

        # ↓ Move DOWN along the right column
        for r in range(top, bottom + 1):
            result.append(matrix[r][right])
        right -= 1

        # ← Move LEFT across the bottom row (if rows remain)
        if top <= bottom:
            for c in range(right, left - 1, -1):
                result.append(matrix[bottom][c])
            bottom -= 1

        # ↑ Move UP along the left column (if cols remain)
        if left <= right:
            for r in range(bottom, top - 1, -1):
                result.append(matrix[r][left])
            left += 1

    print(result)
    return result


# ============================================================
# 6. BOUNDARY TRAVERSAL (Only the outer edge)
# ============================================================
# Visit only the elements on the border of the matrix.
#
# Output: 1 2 3 4 8 12 16 15 14 13 9 5

def traverse_boundary(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []

    # Top row (left to right)
    for c in range(cols):
        result.append(matrix[0][c])

    # Right column (top+1 to bottom)
    for r in range(1, rows):
        result.append(matrix[r][cols - 1])

    # Bottom row (right-1 to left), only if more than 1 row
    if rows > 1:
        for c in range(cols - 2, -1, -1):
            result.append(matrix[rows - 1][c])

    # Left column (bottom-1 to top+1), only if more than 1 column
    if cols > 1:
        for r in range(rows - 2, 0, -1):
            result.append(matrix[r][0])

    print(result)
    return result


# ============================================================
# 7. ZIGZAG TRAVERSAL (Alternating left-right per row)
# ============================================================
# Even rows go left→right, odd rows go right→left.
#
# Output: 1 2 3 4 8 7 6 5 9 10 11 12 16 15 14 13

def traverse_zigzag(matrix):
    rows = len(matrix)
    result = []

    for r in range(rows):
        if r % 2 == 0:
            # Even row → left to right
            result.extend(matrix[r])
        else:
            # Odd row → right to left
            result.extend(matrix[r][::-1])

    print(result)
    return result


# ============================================================
# 8. TRANSPOSE (Rows ↔ Columns)
# ============================================================
# Swap rows and columns: element at (r, c) moves to (c, r).
#
# Original:         Transposed:
# [1,  2,  3,  4]   [1,  5,  9,  13]
# [5,  6,  7,  8]   [2,  6,  10, 14]
# [9,  10, 11, 12]  [3,  7,  11, 15]
# [13, 14, 15, 16]  [4,  8,  12, 16]

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Using list comprehension — creates new matrix
    result = [[matrix[r][c] for r in range(rows)] for c in range(cols)]

    for row in result:
        print(row)
    return result


# ============================================================
# 9. ROTATE 90° CLOCKWISE
# ============================================================
# Step 1: Transpose (swap rows and columns)
# Step 2: Reverse each row
#
# Original:         Rotated 90° CW:
# [1,  2,  3,  4]   [13, 9,  5, 1]
# [5,  6,  7,  8]   [14, 10, 6, 2]
# [9,  10, 11, 12]  [15, 11, 7, 3]
# [13, 14, 15, 16]  [16, 12, 8, 4]

def rotate_90_clockwise(matrix):
    # Transpose
    n = len(matrix)
    for r in range(n):
        for c in range(r + 1, n):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    # Reverse each row
    for r in range(n):
        matrix[r].reverse()

    for row in matrix:
        print(row)
    return matrix


# ============================================================
# 10. 4-DIRECTIONAL NEIGHBORS (BFS/DFS helper)
# ============================================================
# Given a cell (r, c), find its up/down/left/right neighbors.
# Essential for BFS/DFS grid problems.

def get_neighbors_4(matrix, r, c):
    rows = len(matrix)
    cols = len(matrix[0])

    # Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    neighbors = []
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            neighbors.append((nr, nc, matrix[nr][nc]))

    return neighbors


# ============================================================
# 11. 8-DIRECTIONAL NEIGHBORS (includes diagonals)
# ============================================================
# Given a cell (r, c), find ALL 8 surrounding neighbors.
# Used in problems like "mines" or "game of life".

def get_neighbors_8(matrix, r, c):
    rows = len(matrix)
    cols = len(matrix[0])

    directions = [
        (-1, -1), (-1, 0), (-1, 1),   # top-left, top, top-right
        (0, -1),           (0, 1),     # left,          right
        (1, -1),  (1, 0),  (1, 1)      # bot-left, bot, bot-right
    ]

    neighbors = []
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            neighbors.append((nr, nc, matrix[nr][nc]))

    return neighbors


# ============================================================
# SAMPLE DATA & TEST CALLS
# ============================================================
if __name__ == "__main__":

    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    print("=" * 50)
    print("0. SIMPLEST TRAVERSAL (no indices)")
    print("=" * 50)
    traverse_simple(matrix)

    print("\n" + "=" * 50)
    print("1. ROW-WISE TRAVERSAL")
    print("=" * 50)
    traverse_row_wise(matrix)

    print("\n" + "=" * 50)
    print("2. COLUMN-WISE TRAVERSAL")
    print("=" * 50)
    traverse_col_wise(matrix)

    # print("\n" + "=" * 50)
    # print("3. DIAGONAL TRAVERSAL (Top-Left → Bottom-Right)")
    # print("=" * 50)
    # traverse_diagonal(matrix)

    # print("\n" + "=" * 50)
    # print("4. ANTI-DIAGONAL TRAVERSAL (group by r+c)")
    # print("=" * 50)
    # traverse_anti_diagonal(matrix)

    # print("\n" + "=" * 50)
    # print("5. SPIRAL TRAVERSAL")
    # print("=" * 50)
    # traverse_spiral([row[:] for row in matrix])  # pass copy

    # print("\n" + "=" * 50)
    # print("6. BOUNDARY TRAVERSAL")
    # print("=" * 50)
    # traverse_boundary(matrix)

    # print("\n" + "=" * 50)
    # print("7. ZIGZAG TRAVERSAL")
    # print("=" * 50)
    # traverse_zigzag(matrix)

    # print("\n" + "=" * 50)
    # print("8. TRANSPOSE")
    # print("=" * 50)
    # transpose([row[:] for row in matrix])  # pass copy

    # print("\n" + "=" * 50)
    # print("9. ROTATE 90° CLOCKWISE")
    # print("=" * 50)
    # rotate_90_clockwise([row[:] for row in matrix])  # pass copy

    # print("\n" + "=" * 50)
    # print("10. 4-DIRECTIONAL NEIGHBORS of (1,1) → value 6")
    # print("=" * 50)
    # neighbors = get_neighbors_4(matrix, 1, 1)
    # print(f"Neighbors of matrix[1][1]={matrix[1][1]}: {neighbors}")

    # print("\n" + "=" * 50)
    # print("11. 8-DIRECTIONAL NEIGHBORS of (1,1) → value 6")
    # print("=" * 50)
    # neighbors = get_neighbors_8(matrix, 1, 1)
    # print(f"Neighbors of matrix[1][1]={matrix[1][1]}: {neighbors}")
