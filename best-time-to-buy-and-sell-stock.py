from typing import List

# brute force
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         length = len(prices)
   
#         maxProfit = 0
#         for i in range(length): # i === buy date
#             for j in range (i + 1,length): # j === sell date 
#                 print(i, j)
#                 buyPrice = prices[i]
#                 sellPrice = prices[j]


#                 currentSetupProfit = sellPrice - buyPrice
#                 if(currentSetupProfit > maxProfit):
#                     maxProfit = currentSetupProfit

#         return maxProfit
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lowestPrice = prices[0]
        for currentPrice in prices:
            if(currentPrice < lowestPrice):
                lowestPrice = currentPrice
            if(currentPrice - lowestPrice > maxProfit):
                maxProfit = currentPrice - lowestPrice
        return maxProfit

# a bit of note taking
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         length = len(prices)
        
#         priceDict = {}

#         for i in range(length):
#             # create if don't exist
#             if(prices[i] in priceDict):
#                 priceDict[prices[i]].append(i)
#             else:
#                 priceDict[prices[i]] = [i]

#         prices.sort(reverse=True)
#         # print(prices)
#         # print(priceDict)

#         maxProfit = 0
#         for buyPricePointer in range(length - 1, 0, -1):

#             # check best possible
#             bestPossibleProfit = prices[0] - prices[buyPricePointer]
            
#             if(maxProfit >= bestPossibleProfit):
#                 break

#             for sellPricePointer in range(0, buyPricePointer):
#                 # print(buyPricePointer, sellPricePointer)
#                 buyPrice = prices[buyPricePointer]
#                 buyDate = priceDict[buyPrice][0]
                

#                 sellPrice = prices[sellPricePointer]
#                 sellDate = priceDict[sellPrice][len(priceDict[sellPrice]) - 1]


#                 # if sellDate lower than buyDate, it doesn't make sense
#                 if(sellDate <= buyDate):
#                     continue
#                 else:
#                     currentProfit = sellPrice - buyPrice
#                     if(currentProfit > maxProfit):
#                         maxProfit = currentProfit
#                         break


#         return maxProfit

# test it

# test = [1,4,1,4,3,1]
# test = [2,1,2,0,1]
test = [3,2,6,5,0,3]

solution = Solution()
result = solution.maxProfit(test)

print(result)
