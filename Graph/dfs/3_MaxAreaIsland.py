"""
Max Area of Island

Description:
Given a grid of water (0) and land (1), return the area of the largest
island. Land connects horizontally and vertically.

Approach:
1. Scan every cell in the grid.
2. When an unvisited land cell is found, run DFS to return that island's area.
3. In DFS, stop at water, an out-of-bounds position, or a cell already visited.
    Return 0 for these positions. Otherwise mark the land cell visited by
    changing it to 0 and return 1 plus the areas from its four neighbors.
4. Update max_area after each island is explored.
5. Return max_area, or 0 if there are no islands.

Let `R` be the number of rows and `C` the number of columns.

Time Complexity:
1. The nested loops inspect every cell: O(R * C).
2. Across all DFS calls, each land cell is visited once and checks four
    neighbors: O(R * C) total.
3. Updating max_area after each island takes constant time.
Overall: O(R * C).

Space Complexity:
- The grid is marked in place, so no separate visited grid is allocated.
- The recursive DFS call stack can grow to O(R * C) in the worst case.
Overall auxiliary space: O(R * C) worst case due to recursion.
"""

from collections import deque

# **Return-value approach (tree-like DFS)**
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                return 0

            grid[row][col] = 0

            return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(dfs(i, j), max_area)

        return max_area


# **Loop-based Directions - DFS approach**
class SolutionDFSLoop:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                return 0

            grid[row][col] = 0
            area = 1

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr = row + dr
                nc = col + dc
                area += dfs(nr, nc)

            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(dfs(i, j), max_area)

        return max_area


class SolutionBFS:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        qq = deque()

        def bfs(area):
            while qq:
                row, col = qq.popleft()

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr = row + dr
                    nc = col + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        area += 1
                        qq.append((nr, nc))

            return area

        max_area = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    qq.append((i, j))
                    grid[i][j] = 0
                    max_area = max(bfs(1), max_area)

        return max_area


"""
Return-value approach (tree-like DFS) pseudocode:
------------------------------------------------
function maxAreaOfIsland(grid):
    largest_area = 0

    for each cell (row, col) in grid:
        if cell is land and unvisited:
            current_area = dfs(row, col)
            largest_area = max(largest_area, current_area)

    return largest_area

function dfs(row, col):
    if position is outside grid or contains water or is already visited:
        return 0

    mark cell visited by changing it to 0
    return 1 + dfs(down) + dfs(up) + dfs(right) + dfs(left)

Loop-based DFS alternative:
    use the same grid scan, base case, and visited mark
    area = 1
    for each of the four neighboring positions:
        area += dfs(neighbor)
    return area

BFS pseudocode:
---------------
function maxAreaOfIsland(grid):
    queue = empty queue
    largest_area = 0

    bfs(area):
        while queue is not empty:
            remove a cell from the queue
            for each of its four neighbors:
                if neighbor is inside the grid and is unvisited land:
                    mark neighbor visited by changing it to 0
                    area += 1
                    add neighbor to the queue
        return area

    for each cell in grid:
        if cell is unvisited land:
            add cell to the queue and mark it visited
            largest_area = max(bfs(1), largest_area)

    return largest_area

BFS complexity: O(R * C) time and O(R * C) worst-case queue space.
"""
        