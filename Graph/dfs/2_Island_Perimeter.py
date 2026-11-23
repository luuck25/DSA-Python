"""
Island Perimeter

Description:
Given a grid of water (0) and land (1) containing one island, return the
island's perimeter. Land cells connect horizontally and vertically.

Approach:
1. Scan the grid until the first land cell is found, then start DFS from it.
2. For each visited land cell, inspect its four neighboring positions.
3. If a neighbor is outside the grid or is water, that side contributes one
    unit to the perimeter.
4. If a neighbor is unvisited land, continue DFS from it. Mark land as `-1`
    before exploring so the DFS does not visit the same cell repeatedly.
5. Return the accumulated perimeter. This assumes the problem's single-island
    condition; other disconnected land cells are not visited.

Let `R` be the number of rows and `C` the number of columns.

Time Complexity:
1. The scan may inspect up to every grid cell: O(R * C).
2. DFS visits each island cell once and checks four sides per cell: O(I),
    where I is the number of island cells, and I <= R * C.
Overall worst case: O(R * C).

Space Complexity:
- The grid is marked in place, so no separate visited grid is allocated.
- Recursive DFS can use up to O(I) call-stack space, or O(R * C) worst case.
Auxiliary space: O(R * C) worst case due to recursion.

https://www.youtube.com/watch?v=O34v6f6s3lQ&t=1320s

"""

from collections import deque
from typing import List


# Approach: use nonlocal perimeter as a shared variable across DFS calls.
class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0

        def dfs(row, col):
            nonlocal perimeter  # Update the perimeter from islandPerimeter.

            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                perimeter += 1
                return
            if grid[row][col] == -1:
                return

            grid[row][col] = -1

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(row + dr, col + dc)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    dfs(row, col)
                    return perimeter

        return perimeter


# Return-value approach (tree-like DFS)
class SolutionDFSReturn:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                return 1

            if grid[row][col] == -1:
                return 0

            grid[row][col] = -1

            return dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return dfs(row, col)

        return 0


"""
DFS pseudocode:
--------------
function islandPerimeter(grid):
    perimeter = 0

    dfs(row, col):
        if position is outside grid or contains water:
            perimeter += 1
            return
        if cell is already visited (-1):
            return

        mark cell visited (-1)
        dfs(each of the four neighboring positions)

    find the first land cell and call dfs on it
    return perimeter

BFS pseudocode:
--------------
function islandPerimeter(grid):
    perimeter = 0
    find the first land cell
    mark it visited (-1) and add it to the queue

    while queue is not empty:
        remove a land cell from the queue
        for each of its four neighbors:
            if neighbor is outside the grid or is water:
                perimeter += 1
            else if neighbor is unvisited land (1):
                mark neighbor visited (-1)
                add neighbor to the queue

    return perimeter
"""

class SolutionBFS:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0

        def bfs():
            nonlocal perimeter  # Update the perimeter from islandPerimeter.

            while qq:
                row, col = qq.popleft()

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr = row + dr
                    nc = col + dc

                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] == 0:
                        perimeter += 1
                    elif grid[nr][nc] == 1:
                        grid[nr][nc] = -1
                        qq.append((nr, nc))

        qq = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    qq.append((row, col))
                    grid[row][col] = -1
                    bfs()
                    return perimeter

        return perimeter



