"""
Rotting Oranges

Problem:
Grid cells are 0 (empty), 1 (fresh orange), or 2 (rotten orange). Every
minute, a rotten orange rots each 4-directionally adjacent fresh orange.
Return the minutes until no fresh orange remains, or -1 if impossible.

Example:
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]  ->  answer = 4

Approach - multi-source BFS:
Every already-rotten orange starts rotting neighbors at minute 0
simultaneously, so the queue is seeded with ALL of them, not just one.
Two equivalent bookkeeping styles are implemented below - see
01Matrix.py in this folder for an in-depth breakdown of
SolutionTagEachNode vs SolutionBatchByWave and why they always agree.

Note: the answer is the MAXIMUM minute assigned to any orange (when the
LAST one rots), not the distance to one specific target cell.

Complexity: Time O(R * C), Space O(R * C).
"""

import collections
from typing import List


class SolutionBatchByWave:
    """Multi-source BFS that advances one full minute (wave/layer) at a
    time, using a frozen len(q) snapshot as the wave size. `time` is a
    single shared counter incremented once per wave, not per orange.
    """

    def orangesRotting(self, grid: List[List[int]]) -> int:

        q = collections.deque()
        fresh = 0
        time = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and q:
            # Snapshot this minute's wave size BEFORE processing it.
            # Oranges that rot during this loop get appended to the back
            # of the queue, so they belong to the NEXT minute, not this one.
            length = len(q)
            for i in range(length):
                r, c = q.popleft()

                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1:
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1  # The whole wave is done - one full minute has passed
        return time if fresh == 0 else -1


class SolutionTagEachNode:
    """Multi-source BFS that tracks elapsed time by gluing the minute
    directly onto each queue item: (row, col, minute). No wave-snapshot
    loop needed - the answer is simply the MAX minute seen across every
    rot event, since that is when the LAST orange rots.
    """

    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c, 0))  # every initially-rotten orange starts at minute 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        minutes_elapsed = 0

        while q:
            r, c, minute = q.popleft()

            minutes_elapsed = minute

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    # Mutating grid to 2 at push time still does double
                    # duty as "visited", exactly like the wave solution.
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc, minute + 1))

        return minutes_elapsed if fresh == 0 else -1

