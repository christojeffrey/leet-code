
from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        maxHIndex = len(citations)
        valid = False
        while(not valid):
            aboveCount = 0
            for i in range(len(citations)):
                if(citations[i] >= maxHIndex):
                    aboveCount += 1
            # print(aboveCount)
            if(aboveCount >= maxHIndex):
                valid = True
            else:
                maxHIndex -= 1
        return maxHIndex
    
test = [3,0,6,1,5]

sol = Solution()
result = sol.hIndex(test)
print(result)