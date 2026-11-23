"""
01 Matrix
=========

Problem
-------
For each cell in a binary matrix, return the distance to the nearest `0`.
Each move goes up, down, left, or right (4-directional) and has distance 1.
The matrix is guaranteed to contain at least one `0`.

Example
-------
    mat = [[0, 0, 0],
           [0, 1, 0],
           [1, 1, 1]]
    answer = [[0, 0, 0],
              [0, 1, 0],
              [1, 2, 1]]

Why BFS, and why MULTI-source?
--------------------------------
Every move costs exactly 1 - no move is cheaper or more expensive - so BFS
is the right tool, same reasoning as ShortestBinaryPath.py.

The multi-source twist (same idea as Rotting_Oranges.py): there isn't one
starting cell here, there are MANY. Every `0` in the matrix is already at
distance 0, all at once. So instead of dropping a single stone in the
pond, every `0` drops its own stone simultaneously, and all those ripples
expand outward together. The fix is the same as always: seed the BFS
queue with EVERY `0` before the loop even starts, instead of just one.

Two ways to write the exact same multi-source BFS
----------------------------------------------------
(See ShortestBinaryPath.py and Rotting_Oranges.py in this same folder for
the first appearances of these two styles - same idea, applied here.)

1) SolutionTagEachNode - "tag each node" style (the original solution)
   Here the "tag" doesn't ride in a queue tuple - it rides directly in the
   matrix cell itself. Every non-zero cell starts out marked "#"
   (not-yet-assigned). When a neighbor is discovered, its real distance is
   written straight in: `mat[nrr][ncc] = mat[r][c] + 1`. No level loop is
   needed at all, because the parent's own distance is already sitting
   right there in `mat[r][c]` the instant it gets popped - you already
   have the number you need, for free.

2) SolutionBatchByWave - "batch by wave" style (new)
   An external `level` counter tracks the current distance instead. The
   code snapshots `len(q)` before processing a layer - that frozen count
   is exactly how many cells are at the current distance, because next
   layer's newly-discovered cells only get appended to the queue DURING
   this very loop, landing safely outside the frozen range(). Once a full
   wave finishes, `level` ticks up by 1 for everyone. `level` starts at 1
   (not 0) because every `0` cell already encodes distance 0 for free -
   the first wave of neighbors discovered is exactly 1 step away.

Why tag-style is the "natural" choice here (but wave works too - verified)
-----------------------------------------------------------------------------
It would be easy to assume the level/wave approach "can't" work here
because the matrix is being mutated in place - it is not blocked by that
at all. Matrix mutation is doing TWO separate jobs that just happen to
both be solved by writing into the grid:
    a) "has this cell been visited yet?"       -> is it still "#" or not
    b) "what distance number do I write here?" -> either mat[r][c] + 1
                                                   (tag style) or the
                                                   external `level`
                                                   (wave style)
Both styles need (a) identically. They only differ in where (b) gets its
number from. Tag-style is simply less work HERE specifically, because this
problem's own output (the distance grid) already hands you the number you
need for free - there's nothing to gain by tracking it a second time in an
external counter. Contrast with Rotting_Oranges.py, where the grid's `1`/
`2` values carry no distance information at all, so SOMETHING external
(a tuple-tag or a wave counter) is genuinely required there.

Verified empirically: both solutions below produce identical output on
every fixed test case and on 500+ random matrices in scratch testing.

Complexity (both solutions)
----------------------------
Time:  O(R * C) - each cell is enqueued and processed at most once, and
       each processing step checks a constant 4 neighbors.
Space: O(R * C) - the queue can hold every cell in the worst case.
       Distances and visited markers are stored in the input matrix - no
       separate distance or visited matrix is allocated by either style.
Both solutions modify the input matrix in place.

References
----------
https://www.youtube.com/watch?v=hIvMZFqjs_A
https://www.youtube.com/watch?v=gu2MD0mpy9w
"""

from collections import deque
from typing import List


class SolutionTagEachNode:
    """Multi-source BFS where the matrix cell itself IS the distance tag.
    No level loop needed - mat[r][c] already holds the parent's distance
    the instant it is popped, so a neighbor's distance is just
    mat[r][c] + 1, read straight off the grid.
    """

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        row_len = len(mat)
        col_len = len(mat[0])

        queue = deque()

        for row in range(row_len):
            for col in range(col_len):
                if mat[row][col] == 0:
                    queue.append((row, col))
                else:
                    mat[row][col] = '#'

        while queue:

            # dont need for loop as results are stored directly in grid

            r, c = queue.popleft()

            neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for nr, nc in neighbours:
                nrr, ncc = r + nr, c + nc

                if 0 <= nrr < row_len and 0 <= ncc < col_len and mat[nrr][ncc] == "#":
                    mat[nrr][ncc] = mat[r][c] + 1
                    queue.append((nrr, ncc))
        return mat


class SolutionBatchByWave:
    """Multi-source BFS that advances one full distance (wave/layer) at a
    time, using a frozen len(queue) snapshot as the wave size. An external
    `level` counter supplies the distance written into each newly
    discovered cell, instead of reading it off the parent cell.
    """

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        row_len = len(mat)
        col_len = len(mat[0])

        queue = deque()

        for row in range(row_len):
            for col in range(col_len):
                if mat[row][col] == 0:
                    queue.append((row, col))
                else:
                    mat[row][col] = '#'

        neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        level = 1  # every 0-cell already encodes distance 0 for free; next wave is distance 1

        while queue:
            # Snapshot this wave's size BEFORE processing it. Cells
            # discovered during this loop get appended to the back of the
            # queue, so they belong to the NEXT wave, not this one.
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for nr, nc in neighbours:
                    nrr, ncc = r + nr, c + nc

                    if 0 <= nrr < row_len and 0 <= ncc < col_len and mat[nrr][ncc] == "#":
                        mat[nrr][ncc] = level  # comes from the external counter, not mat[r][c] + 1
                        queue.append((nrr, ncc))

            level += 1  # the whole wave is done - move to the next distance

        return mat

