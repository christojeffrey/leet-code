
from typing import List

class Solution:
    def jump(self, nums: List[int]) -> bool:
        maxNextLocationList = []
        for i in range(0, len(nums)):
            maxNextLocationList.append(i + nums[i])
        print(maxNextLocationList)



        maxNextLocation = maxNextLocationList[0]
        if len(nums) == 1:
            return 0
        
        currentIndex = 0
        jumpTaken = 1
        while(maxNextLocation < len(nums) - 1):
            jumpTaken += 1
       
            newMax = 0
            for i in range(currentIndex + 1, maxNextLocation + 1):
                if(maxNextLocationList[i] > newMax):
                    newMax = maxNextLocationList[i]
                    currentIndex = i
            # print("newMax")
            # print(newMax)
            maxNextLocation = newMax

        return jumpTaken

    


# test it
test = [7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]
# test = [2,3,1,1,4]

# test = [1,2]
solution = Solution()
result = solution.jump(test)
print('result')
print(result)