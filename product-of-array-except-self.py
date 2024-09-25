
from typing import List
# check solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1 for i in nums]
        curr = 1
        for i in range(0, len(nums)):
            ans[i] *= curr
            curr *= nums[i]
        print(ans)
        curr = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= curr
            curr *= nums[i]
        return ans
    

test = [1,2,3,4]
sol = Solution()
result = sol.productExceptSelf(test)
print(result)