"""
Game of Life (LeetCode #289)
==============================
Problem:
    Apply Conway's Game of Life rules simultaneously to a board. In-place.
    Rules (based on 8 neighbors):
      - Live cell + <2 live neighbors → dies (underpopulation)
      - Live cell + 2 or 3 neighbors → lives
      - Live cell + >3 neighbors → dies (overpopulation)
      - Dead cell + exactly 3 neighbors → becomes alive (reproduction)

Logic:
    Can't update cells one by one — all updates are simultaneous.
    Use state encoding to store old AND new state in the same cell:
      0 = was dead,  stays dead
      1 = was alive, stays alive
      2 = was alive, now dead       (original = 1, new = 0)
      3 = was dead,  now alive      (original = 0, new = 1)

    Key: original state = value in {1, 2} means "was alive"
    After processing: board[r][c] % 2 gives the NEW state.

Time:  O(m × n)
Space: O(1)

https://thita.ai/problems/game-of-life/editorial
"""

from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0),  (1, 1)]  # 8 neighbors

        rows = len(board)
        cols = len(board[0])

        # Pass 1: encode transitions using 2 and 3
        for r in range(rows):
            for c in range(cols):
                live_neigh = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if board[nr][nc] in (1, 2):  # 1=alive, 2=was alive (now dying)
                            live_neigh += 1

                if board[r][c] == 1:                  # currently alive
                    if live_neigh < 2 or live_neigh > 3:
                        board[r][c] = 2               # alive → dead
                else:                                  # currently dead
                    if live_neigh == 3:
                        board[r][c] = 3               # dead → alive

        # Pass 2: decode — % 2 converts {0→0, 1→1, 2→0, 3→1}
        for r in range(rows):
            for c in range(cols):
                board[r][c] %= 2

    # ---- Clean version (no comments) ----
    def gameOfLife_clean(self, board: List[List[int]]) -> None:
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                      (0, 1), (1, -1), (1, 0), (1, 1)]
        rows, cols = len(board), len(board[0])

        for r in range(rows):
            for c in range(cols):
                live_neigh = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if board[nr][nc] in (1, 2):
                            live_neigh += 1
                if board[r][c] == 1:
                    if live_neigh < 2 or live_neigh > 3:
                        board[r][c] = 2
                else:
                    if live_neigh == 3:
                        board[r][c] = 3

        for r in range(rows):
            for c in range(cols):
                board[r][c] %= 2

        