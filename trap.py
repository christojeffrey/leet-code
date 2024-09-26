from typing import List

# TLE
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         stack = [] # tracking the left wall
#         water = 0
#         for i in range(len(height)):
#             current = (height[i], i)

#             while(True):
#                 # print(stack)
#                 if(len(stack) == 0):
#                     break
#                 top = stack[-1]
#                 if(top[0] <= current[0]):
#                     water += current[1] - top[1] - 1
#                     stack.pop()
#                 else: # if the top is higher
#                     break
                
#             # push the new wall
#             for wall in range(height[i], -1, -1):
#                 print(i)
#                 stack.append((wall, i))

           
#             print(stack)
#         return water


sol = Solution()
ans = sol.trap([4,2,0,3,2,5])

print(ans)



# TLE
class Solution:
    def trap(self, height: List[int]) -> int:
        pass