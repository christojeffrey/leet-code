from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:


        max = 0
        # for leftIndex in range(len(height)):
        #     for rightIndex in range(leftIndex, len(height)):
        #         volume = (rightIndex - leftIndex) * min(height[leftIndex], height[rightIndex])
        #         if(volume > max):
        #             max = volume

        leftIndex = 0
        rightIndex = len(height) - 1

        while(leftIndex != rightIndex):
            volume = (rightIndex - leftIndex)* min(height[leftIndex], height[rightIndex])
            if(volume > max):
                max = volume

            if(height[leftIndex] < height[rightIndex]):
                leftIndex += 1
            else:
                rightIndex -= 1 
        return max