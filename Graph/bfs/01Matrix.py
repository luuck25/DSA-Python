from collections import deque

# https://www.youtube.com/watch?v=hIvMZFqjs_A

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        row_len = len(mat)
        col_len = len(mat[0])

        queue = deque()

        for row in range(row_len):
            for col in range(col_len):
                if mat[row][col] == 0:
                    queue.append((row,col))
                else:
                    mat[row][col] = '#'

        while queue:

            r,c = queue.popleft()  

            neighbours = [(0,1),(0,-1),(1,0),(-1,0)]

            for nr,nc in neighbours:
                nrr , ncc = r + nr , c + nc

                if  0 <= nrr < row_len and 0 <= ncc < col_len and mat[nrr][ncc] == "#"  :
                    mat[nrr][ncc] = mat[r][c] + 1
                    queue.append((nrr,ncc)) 
        return mat        



        