from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # firstNumberIndex = 0
        # for firstIndex in range(len(numbers)):
        #     if(numbers[firstIndex] > target):
        #         # it will not find it
        #         return [-1, -1]
        #     else:
        #         # find the second pointer
        #         for secondIndex in range(firstIndex + 1, len(numbers)):
        #             total = numbers[firstIndex] + numbers[secondIndex]
                    
        #             if(total == target):
        #                 return [firstIndex + 1, secondIndex + 1]
        #             if(total > target):
        #                 break

        left = 0
        right = len(numbers) - 1
        while(True):
            total = numbers[left] + numbers[right]
            if(total > target):
                right -= 1
            elif (total < target):
                left += 1
            else:
                break

        return [left + 1, right + 1]
        

sol = Solution()

ans = sol.twoSum([2,7,11,15], 9)
print(ans)