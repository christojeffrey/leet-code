from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        
        tracker = {}
        trackerColumn = {}
        for i in range(9):
            # reset tracker
            for index in range(9):
                tracker[index + 1] = False

            for index in range(9):
                trackerColumn[index + 1] = False

            for j in range(9):

                # check row
                if (board[i][j] != '.'):
                    number = int(board[i][j])
                    
                    if(tracker[number]):
                        return False
                    
                    tracker[number] = True

                # check column
                if (board[j][i] != '.'):
                    number = int(board[j][i])
                    if(trackerColumn[number]):
                        return False
                    
                    trackerColumn[number] = True
           
    
        # check 3 x 3 box

        for i in range(3):
            for j in range(3):
                startRow = i * 3
                startColumn = j * 3
                
                for index in range(9):
                    tracker[index + 1] = False

                for rowIndex in range(startRow,startRow + 3):
                    for columnIndex in range(startColumn, startColumn + 3):
                        if (board[rowIndex][columnIndex] != '.'):
                            number = int(board[rowIndex][columnIndex])
                            
                            if(tracker[number]):
                                return False
                            
                            tracker[number] = True
          
        return True

sol = Solution()
ans = sol.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
print(ans)