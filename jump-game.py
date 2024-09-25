
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxJump = 1
        currentIndex = 0

        while(maxJump > 0 and currentIndex <= len(nums) - 1):
            maxJump -= 1
            if(nums[currentIndex] > maxJump):
                maxJump = nums[currentIndex]
            currentIndex += 1
        

        if(currentIndex > len(nums) - 1):
            return True
        else:
            return False


# test it

test = [3,2,1,0,4]

solution = Solution()
result = solution.canJump(test)

print(result)