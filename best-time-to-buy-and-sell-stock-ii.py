from typing import List

    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = prices[0]
        for currentPrice in prices[1:]:
            if (currentPrice > lowest):
                profit += currentPrice - lowest
            lowest = currentPrice

        return profit
    
test = [7,6,4,3,1]

solution = Solution()
result = solution.maxProfit(test)

print(result)
