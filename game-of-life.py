from typing import List
import math
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        height = len(board)
        width = len(board[0])
        for i in range(height):
            for j in range(width):
                liveNeighbor = 0
                for rowChanger in range(-1, 2):
                    for colChanger in range(-1, 2):
                        # print(rowChanger, colChanger)
                        if((rowChanger == 0 and colChanger == 0) or i + rowChanger < 0 or i + rowChanger > height - 1 or j + colChanger < 0 or j + colChanger > width - 1):
                            continue

                        if(board[i + rowChanger][j + colChanger] % 2 == 1):
                            liveNeighbor += 1

                print(i, j, liveNeighbor)
                if(board[i][j] == 1):
                    if(liveNeighbor == 2 or liveNeighbor == 3):
                            board[i][j] += 2
                if(board[i][j] == 0):
                    if(liveNeighbor == 3):
                            board[i][j] += 2


        for i in range(height):
            for j in range(width):
                board[i][j] = math.floor(board[i][j]/2)

sol = Solution()
input = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
sol.gameOfLife(input)
print(input)
