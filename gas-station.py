from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # check if it's possible to finish the circuit O(n)
        # condition one - total cost more than total gas
        if(sum(gas) < sum(cost)):
            return -1
    
        # condition two - each gas is lower than each cost
        isPossible = False
        for i in range(len(gas)):
            if(gas[i] >= cost[i]):
                isPossible = True
        
        if(not isPossible):
            return -1
        
        # stupid greedy approach - find the most profit. no checking
        ans = 0
        inTank = 0
        for i in range(len(gas)):
            profit = gas[i] - cost[i]
            if inTank + profit < 0:
                ans = -1
                inTank = 0
                ans = i + 1
            else:
                inTank += profit


        return ans

gas = [3,1,1]
cost = [1,2,2]

sol = Solution()
ans = sol.canCompleteCircuit(gas, cost)
print(ans)