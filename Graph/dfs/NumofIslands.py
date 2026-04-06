class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:

        row_len = len(grid)
        col_len = len(grid[0])

        count = 0


        def dfs(grid,r,c):

            if r < 0 or c < 0 or r >= row_len or c >= col_len or grid[r][c] !='1':
                return

            grid[r][c] = '0'

            dfs(grid,r+1,c)            
            dfs(grid,r,c-1)
            dfs(grid,r-1,c)
            dfs(grid,r,c+1)


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    count += 1
                    dfs(grid,row,col)

        return count