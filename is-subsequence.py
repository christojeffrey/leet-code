class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        while(len(t) != 0 and len(s) != 0):
            if(t[0] == s[0]):
                s = s[1:]
            t = t[1:]

        if(len(s) == 0):
            return True
        
        return False
    