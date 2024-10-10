class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ''

        left = 0
        leftChar = ''
        tracker = {}
        target = {}
        current = {}
        for char in t:
            tracker[char] = False
            current[char] = 0
            if char in target:
                target[char] += 1
            else:
                target[char] = 1

        # move left to the first one
        for index in range(len(s)):
            char = s[index]

            if(char in tracker): # part of target
                left = index
                leftChar = char
                break
        
        right = left

        while(True): 
            complete = True
            # check if complete
            for key in target:
                if(current[key] < target[key]):
                    complete = False
                    break
            
            if(complete):
                currentWindow = s[left:right]
                # check if smaller
                if(ans == '' or len(currentWindow) < len(ans)):
                    ans = currentWindow

                # continue check the next substring 
                found = False
                while(not found):
                    left += 1
                    if(left >= len(s)):
                        break

                    if(s[left] in tracker):
                        found = True
                        
                        # update the current
                        current[leftChar] -= 1

                        leftChar = s[left]
                        break
                if(left >= len(s)):
                    break       
            else:
                if(right >= len(s)):
                    break
                char = s[right]
                if(char in target):
                    current[char] += 1
                    
                right += 1
        return ans

sol = Solution()
ans = sol.minWindow("aa", "a")
print("ans", ans)