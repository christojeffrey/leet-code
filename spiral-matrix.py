from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        width = len(matrix[0])
        height = len(matrix)

        ans = []
        direction = 'right'


        i = 0
        j = 0
        ans.append(matrix[i][j])
        matrix[i][j] = None

        while(len(ans) < width * height):
            # move in direction
            nextI = i
            nextJ = j
            if(direction == 'right'):
                nextJ += 1
            elif(direction == 'down'):
                nextI += 1
            elif(direction == 'left'):
                nextJ -= 1
            elif(direction == 'up'):
                nextI -= 1

            # if turns out it's over the limit, or it has been checked already,
            # update the direction
            if(nextI < 0 or nextI > height - 1 or nextJ < 0 or nextJ > width - 1 or matrix[nextI][nextJ] == None):
                if(direction == 'right'):
                    direction = 'down'
                    nextJ = j
                    nextI += 1
                elif(direction == 'down'):
                    direction = 'left'
                    nextI = i
                    nextJ -= 1
                elif(direction == 'left'):
                    direction = 'up'
                    nextJ = j
                    nextI -= 1
                elif(direction == 'up'):
                    direction = 'right'
                    nextI = i
                    nextJ += 1
                


            # add to answer
            ans.append(matrix[nextI][nextJ])
            i = nextI
            j = nextJ
            matrix[nextI][nextJ] = None

        return ans


sol = Solution()
ans = sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(ans)