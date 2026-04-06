class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])

        result = 0



        def dfs(grid,r,c):

            if r < 0 or c < 0 or r >= row_len or c >= col_len or grid[r][c] !=1:
                
                return 0

            else:
                grid[r][c] = 0
                area = 1
                

            area += dfs(grid,r+1,c)            
            area += dfs(grid,r,c-1)
            area += dfs(grid,r-1,c)
            area += dfs(grid,r,c+1)

            return area
            
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                   result = max(result, dfs(grid,row,col))

        return result
        