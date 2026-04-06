class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

        rows = len(board)
        cols = len(board[0])    

        for r in range(rows):
            for c in range(cols):
                live_neigh = 0
                for dr,dc in directions:
                    nr,nc = r + dr , c+dc
                    if 0 <= nr < rows and 0 <=nc< cols:
                        if board[nr][nc] == 1 or board[nr][nc] == 2:
                            live_neigh += 1

                if board[r][c] ==1:
                    if live_neigh < 2 or live_neigh > 3:
                            board[r][c] = 2
                else:
                    if  live_neigh ==3:
                            board[r][c] = 3

        for r in range(rows):
            for c in range(cols):
                board[r][c] %= 2 






        