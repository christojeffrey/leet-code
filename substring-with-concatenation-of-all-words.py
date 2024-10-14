from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans = []

        tracker = {}
        for word in words:
            if(word not in tracker):
                tracker[word] = 0
            tracker[word] += 1


        for startCharIndex in range(len(words[0])):
            windowTracker = {}
            insideWindow = 0
            for startIndex in range(0, len(s), len(words[0])):
                startIndex += startCharIndex
                currentWord = s[startIndex:startIndex + len(words[0])]
                
                if(currentWord not in windowTracker):
                    windowTracker[currentWord] = 0
                
                windowTracker[currentWord] += 1
                insideWindow += 1

                if(insideWindow > len(words)):
                    wordToRemove = s[startIndex - (len(words[0]) * len(words)) :startIndex + len(words[0]) - (len(words[0]) * len(words))]
                    windowTracker[wordToRemove] -= 1
                    insideWindow -= 1
                    if(windowTracker[wordToRemove] == 0):
                        del windowTracker[wordToRemove]
                
                    
                # print(tracker, windowTracker)
                if(tracker == windowTracker):
                    ans.append(startIndex - (len(words[0]) * (len(words) - 1)))

        return ans  


sol = Solution()
ans = sol.findSubstring(s = "barfoothefoobarman", words = ["foo","bar"])
print(ans)