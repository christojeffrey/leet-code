from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        


        groupsCharFreq = []

        result = []

        for str in strs:

            # does str part of one of the existing group?
            currentStrFreq = {}

            for char in str:
                if(char not in currentStrFreq):
                    currentStrFreq[char] = 0

                currentStrFreq[char] += 1

            found = False
            matchIndex = 0
            for index in range(len(groupsCharFreq)):
                groupCharFreq = groupsCharFreq[index]
                

                identical = True
                # check if it's an identical dict
                for key in groupCharFreq:
                    # the same key exist, and it has the same value

                    if(key not in currentStrFreq):
                        identical = False
                        break
                    if(groupCharFreq[key] != currentStrFreq[key]):
                        identical = False
                        break

                for key in currentStrFreq:
                    # the same key exist, and it has the same value
                    if(key not in groupCharFreq):
                        identical = False
                        break
                    if(groupCharFreq[key] != currentStrFreq[key]):
                        identical = False
                        break
                
                if(identical):
                    found = True
                    matchIndex = index
                    break
            

            # if it's an anagram of existing group, append it
            if(found):
                result[matchIndex].append(str)
            else:
                newGroup = [str]
                groupsCharFreq.append(currentStrFreq)
                result.append(newGroup)
        
        return result

            

sol = Solution()
ans = sol.groupAnagrams(["a"])
print(ans)