"""
Shortest Path in a Binary Matrix

Problem:
Given an n x n binary matrix `grid`, find the length of the shortest path
from (0, 0) to (n-1, n-1), stepping only on 0-cells, moving in any of the
8 directions (4 straight + 4 diagonal). Length = number of cells visited,
including start and end. Return -1 if no such path exists.

Example:
    grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]  ->  answer = 4
    (0,0) -> (0,1) -> (1,2) -> (2,2)  - the diagonal hop is what saves a step.

Approach - single-source BFS:
Every move costs exactly 1 step, so the first time BFS reaches a cell is
guaranteed to be via the fewest possible steps. Two equivalent bookkeeping
styles are implemented below - see 01Matrix.py in this folder for an
in-depth breakdown of SolutionTagEachNode vs SolutionBatchByWave and why
they always agree.

Complexity: Time O(n^2), Space O(n^2).
"""

from collections import deque
from typing import List


class SolutionBatchByWave:
    """BFS that tracks distance by processing the queue one full wave
    (layer) at a time, using a frozen len(queue) snapshot as the wave
    size. Marks cells visited by mutating the input grid in place.
    """

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])

        # Edge case: Start or end is blocked
        if grid[0][0] != 0 or grid[row_len - 1][col_len - 1] != 0:
            return -1

        # Edge case: 1x1 grid
        if row_len == 1 and col_len == 1:
            return 1

        queue = deque([(0, 0)])
        grid[0][0] = 1  # Mark as visited
        level = 1  # Start at level 1 (the first cell)

        neig = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1))

        while queue:
            # Snapshot the current wave size BEFORE processing it. New
            # cells discovered during this loop get appended to the back
            # of the queue, so they fall outside this iteration's fixed
            # range() - they belong to the NEXT wave, not this one.
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for x, y in neig:
                    nr, nc = r + x, c + y

                    # Check if neighbor is within bounds and is an open path
                    if 0 <= nr < row_len and 0 <= nc < col_len and grid[nr][nc] == 0:

                        # --- THE OPTIMIZATION ---
                        # Check if THIS neighbor is the exit BEFORE adding it to queue
                        if nr == row_len - 1 and nc == col_len - 1:
                            return level + 1

                        grid[nr][nc] = 1  # Mark visited
                        queue.append((nr, nc))

            level += 1  # The whole wave is done - move to the next distance

        return -1


class SolutionTagEachNode:
    """BFS that tracks distance by gluing it directly onto each queue
    item: (row, col, distance). No wave-snapshot loop needed - whoever
    pops a cell already knows exactly how far it is from the start.
    Uses a separate `visited` set, so the input grid is left untouched.
    """

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Edge case: Start or end is blocked
        if grid[0][0] != 0 or grid[n - 1][n - 1] != 0:
            return -1

        # Edge case: 1x1 grid
        if n == 1:
            return 1

        directions = (
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1),
        )

        # Each queue item is self-describing: it already knows its own
        # distance, so there is no need to process the queue "one wave at
        # a time" - just read dist straight off whatever gets popped.
        queue = deque([(0, 0, 1)])
        visited = {(0, 0)}

        while queue:
            
            r, c, dist = queue.popleft()

            if (r, c) == (n - 1, n - 1):
                return dist

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in visited:
                    # Mark visited at PUSH time (discovery time), not pop
                    # time - this guarantees a cell is enqueued exactly
                    # once, carrying its shortest possible distance.
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))

        return -1

