from collections import deque
from typing import List

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])

        # Edge case: Start or end is blocked
        if grid[0][0] != 0 or grid[row_len-1][col_len-1] != 0:
            return -1
        
        # Edge case: 1x1 grid
        if row_len == 1 and col_len == 1:
            return 1

        queue = deque([(0, 0)]) 
        grid[0][0] = 1 # Mark as visited
        level = 1 # Start at level 1 (the first cell)

        neig = ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1))
        
        while queue:
            # Snapshot of the current level
            # loop is needed as its for each level
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
                        
                        grid[nr][nc] = 1 # Mark visited
                        queue.append((nr, nc))
            
            level += 1 # Move to the next distance
            
        return -1