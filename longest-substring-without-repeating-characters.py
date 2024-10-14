class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        

        leftIndex = 0
        tracker = {}
        maximum = 0
        for rightIndex in range(len(s)):

            # if currentwindow is not unique, majuin the left one
            isUnique = s[rightIndex] not in tracker

            while(not isUnique):
                del tracker[s[leftIndex]]
                leftIndex += 1
                isUnique = s[rightIndex] not in tracker
            
            tracker[s[rightIndex]] = True

            # print(leftIndex, rightIndex)

            maximum = max(maximum, rightIndex - leftIndex + 1)
    
        return maximum
    
sol = Solution()
ans = sol.lengthOfLongestSubstring("abcabcbb")
print(ans)