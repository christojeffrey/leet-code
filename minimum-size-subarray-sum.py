from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        leftIndex = 0
        min = 0
        found = False
        total = 0
        for rightIndex in range(len(nums)):
            total += nums[rightIndex]
            while (total >= target):
                currentMin = rightIndex - leftIndex + 1
                
                if(not found or currentMin < min):
                    found = True
                    min = currentMin
                total -= nums[leftIndex]
                leftIndex += 1
        return min


sol = Solution()

ans = sol.minSubArrayLen(7, [2,3,1,2,4,3])
print(ans)