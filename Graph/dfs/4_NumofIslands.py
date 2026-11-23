"""
Number of Islands

Description:
Given a grid of "1" (land) and "0" (water), count the islands. Land cells
belong to the same island when connected horizontally or vertically.

Approach:
1. Scan every cell in the grid.
2. When an unvisited land cell is found, it starts a new island, so increment
    the island count.
3. Run DFS from that cell to visit all connected land cells. Mark each visited
    cell as "0" in the grid so it will not be counted again.
4. Continue scanning. Return the number of DFS starts.

Let `R` be the number of rows and `C` the number of columns. This implementation
assumes the grid is nonempty and modifies it in place.

Time Complexity:
1. The nested loops inspect every cell: O(R * C).
2. Across all DFS calls, each land cell is visited once and checks four
    neighbors: O(R * C) total.
Overall: O(R * C).

Space Complexity:
- The grid itself is used to mark visited cells, so no separate visited grid
  is allocated.
- The recursive DFS stack can grow to O(R * C) in the worst case.
Auxiliary space: O(R * C) worst case due to recursion.
"""

from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == "0":
                return

            grid[row][col] = "0"

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1

        return islands


# **Loop-based Directions - DFS approach**
class SolutionDFSLoop:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == "0":
                return

            grid[row][col] = "0"

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr = row + dr
                nc = col + dc
                dfs(nr, nc)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    islands += 1

        return islands


# **BFS approach**
class SolutionBFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        qq = deque()

        def bfs():
            while qq:
                row, col = qq.popleft()

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr = row + dr
                    nc = col + dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        qq.append((nr, nc))

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    grid[i][j] = "0"
                    qq.append((i, j))
                    bfs()
                    islands += 1

        return islands


"""
Pseudocode:
-----------
function numIslands(grid):
    island_count = 0

    for each cell (row, col) in grid:
        if grid[row][col] is unvisited land:
            dfs(row, col)
            island_count += 1

    return island_count

function dfs(row, col):
    if position is outside grid or contains water or was already visited:
        return

    mark cell visited by changing it to "0"
    dfs(down)
    dfs(up)
    dfs(right)
    dfs(left)

Direction-loop DFS alternative:
    replace the four calls with a loop over down, up, right, and left
    dfs(each neighboring position)

BFS pseudocode:
---------------
function numIslands(grid):
    island_count = 0
    queue = empty queue

    bfs():
        while queue is not empty:
            remove a cell from the queue
            for each of its four neighbors:
                if neighbor is inside the grid and is land ("1"):
                    mark neighbor visited ("0") before enqueueing
                    add neighbor to the queue

    for each cell in grid:
        if cell is land ("1"):
            mark cell visited ("0")
            add cell to the queue
            bfs()
            island_count += 1

    return island_count

BFS complexity: O(R * C) time and O(R * C) worst-case queue space.
"""
