from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        highestFromLeft = []
        
        currentHighest = height[0]


        for wallHeight in height:

            if(wallHeight > currentHighest):
                currentHighest = wallHeight
            highestFromLeft.append(currentHighest)
        
        highestFromRight = []
        
        currentHighest = height[len(height) - 1]
        height.reverse()
        for wallHeight in height:
            if(wallHeight > currentHighest):
                currentHighest = wallHeight
            highestFromRight.append(currentHighest)

        highestFromRight.reverse()

        height.reverse()

        water = 0
        for index in range(len(height)):
            water += max(0, min(highestFromLeft[index], highestFromRight[index]) - height[index])
        
        return water

        
        


sol =Solution()
ans = sol.trap([4,2,0,3,2,5])
print(ans)