class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        tmp = [row[:]  for row in matrix]

        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            for j in range(col):

                if matrix[i][j] == 0:
                    for k in range(col):
                        tmp[i][k] =0  # ith row zero
                    for k in range(row):
                        tmp[k][j] = 0         #jth col zero

        # copy back to original matrix
        for i in range(row):
            for j in range(col):
                matrix[i][j] = tmp[i][j]               



 class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        firstRowImpacted = False
        firstColImpacted = False
        
        if len(matrix) ==0:
            return

        row = len(matrix)
        col = len(matrix[0])

        print(col)
        for c in range(col) :
            print(c)

            if matrix[0][c] == 0:
                firstRowImpacted = True
                break
                
        for r in range(row) :
            if matrix[r][0] == 0:
                firstColImpacted = True
                break

        # set markers for first row and col

        for r in range(1, row):
            for c in range(1,col):

                if matrix[r][c] == 0:
                    matrix[r][0] =0
                    matrix[0][c] =0
        # iterate without first row and col

        for r in range(1,row):
            for c in range(1,col):

                if matrix[0][c] ==0 or matrix[r][0] ==0 :
                    matrix[r][c] =0      

        if  firstRowImpacted:

            for col in range(0,col):
                matrix[0][col] =0

        if firstColImpacted:
            for row  in range(0,row):
                matrix[row][0] = 0


                                       