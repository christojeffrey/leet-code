from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        currentStart = None
        currentNumber = None
        ans = []

        
        for index in range(len(nums)):
            num = nums[index]
            if(currentStart == None):
                currentStart = num
                currentNumber = num

            if(num == currentNumber + 1):
                currentNumber = num
            
            if(index == len(nums) - 1 or nums[index + 1] != currentNumber + 1):
                if(num == currentStart):
                    ans.append(str(num))
                else:
                    ans.append(str(currentStart) + "->" + str(num))
                    
                currentNumber = None
                currentStart = None
            

        return ans


sol = Solution()
ans = sol.summaryRanges([0,2,3,4,6,8,9])
print(ans)