class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        
        row , col = 0,0

        m = len(mat)
        n = len(mat[0])

        up = True
        result = []

        for _ in range(m*n):

            result.append(mat[row][col])

            if up:

                if col == n - 1:
                    row += 1
                    up = False
                elif row == 0:
                    col += 1
                    up = False                    
                else:
                    row -= 1
                    col += 1    
            else:


                if row == m -1:
                    col += 1
                    up = True
                elif col == 0:
                    row += 1
                    up = True                    
                else:
                    row += 1
                    col -= 1     
        return result                       

"""
etter to follow standard order:

if col == n - 1:
elif row == 0:

👉 Why?

At top-right corner, both are true
Correct move should be go down, not right

"""