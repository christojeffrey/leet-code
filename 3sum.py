from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # create dictionary of num and it's index
        result = []
        nums.sort()
        dictionaryOfNum = {}
        for index, num in enumerate(nums):
            dictionaryOfNum[num] = index
        testedI = {}

        dictonaryOfResult = {}
        
        for i in range(0, len(nums)):
            if nums[i] in testedI.keys():
                continue
            testedI[nums[i]] = 1
            for j in range(i + 1, len(nums)):
                # find in dict
                if(-(nums[i] + nums[j])) in dictionaryOfNum.keys():
                    # check if index is larger than j
                    k = dictionaryOfNum[-(nums[i] + nums[j])]
                    if(k > j):
                        newRes = [nums[i], nums[j], nums[k]]
                        newResStr= ''.join(str(x) for x in newRes)
                        if newResStr not in dictonaryOfResult.keys():
                            result.append(newRes)
                            dictonaryOfResult[newResStr] = 1               
        
        return result
                       
        


sol = Solution()
res = sol.threeSum([1,-1,-1,0])
print(res)

