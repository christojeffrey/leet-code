from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        height = len(matrix)
        width = len(matrix[0])
        nextZero = [[False for _ in range(width)] for _ in range(height)]

        for i in range(height):
            for j in range(width):
                if(matrix[i][j] == 0):
                    for colIndex in range(width):
                        nextZero[i][colIndex] = True
                    for rowIndex in range(height):
                        nextZero[rowIndex][j] = True
        for i in range(height):
            for j in range(width):
                if(nextZero[i][j]):
                    matrix[i][j] = 0
