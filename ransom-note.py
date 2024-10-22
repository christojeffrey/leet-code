class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineDict = {}
        for char in magazine:
            if char in magazineDict:
                magazineDict[char] += 1
            else:
                magazineDict[char] = 1


        for char in ransomNote:
            if char in magazineDict:
                magazineDict[char] -= 1
                if magazineDict[char] < 0:
                    return False
            else:
                return False
        return True
