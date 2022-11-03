class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix) - 1): # row index
            for j in range(len(matrix[0]) - 1): # column index
                if matrix[i][j] != matrix[i + 1][j + 1]: # compare diagonal elements in the matrix
                    return False # if any diagonal element is not equal, return False
        return True # if all diagonal elements are equal, return True
