class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        isPreviousSpace = s[0] == ' '

        for character in s:
            if(character != ' '):
                # if current not space, update the length: you can add by 1, or make it 1
                if (not isPreviousSpace):
                    length += 1
                else:
                    length = 1
            
                isPreviousSpace = False
            else:
                isPreviousSpace = True

        return length