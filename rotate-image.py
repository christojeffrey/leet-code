from typing import List
import math
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(math.ceil(n/2)):
            for j in range(math.floor(n/2)):
                first = matrix[i][j]
                second = matrix[j][n - i - 1]
                third = matrix[n - i - 1][n - j - 1]
                fourth = matrix[n - j - 1][i]
                temp = fourth
                matrix[n - j - 1][i] = third
                matrix[n - i - 1][n - j - 1] = second
                matrix[j][n - i - 1] = first
                matrix[i][j] = temp
