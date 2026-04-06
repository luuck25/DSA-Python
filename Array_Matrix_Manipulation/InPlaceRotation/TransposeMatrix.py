class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row  = len(matrix)
        col = len(matrix[0])

        res = [[0] * row for _ in range(col)]

        for i in range(row):
            for j in range(col):
                res[j][i] = matrix[i][j]
        return res        
        


def transposeInPlace(matrix): # only if square matrix
    n = len(matrix)
    
    for i in range(n):
        for j in range(i + 1, n): # i+1 to avoid 2 swaps
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]        
