class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = ''
        if(numRows == 1):
            return s
        for row in range(numRows):
            goDownJump = (numRows - row - 1) * 2
            goUpJump = (row) * 2
            

            i = row
            if(i >= len(s)):
                break
            ans += s[i]

            if(goUpJump > 0 or goDownJump > 0):

                while(True):
                    if(goDownJump > 0):
                        i += goDownJump
                        if(i >= len(s)):
                            break
                        ans += s[i]


                    if(goUpJump > 0):
                        i += goUpJump
                        if(i >= len(s)):
                            break
                        ans += s[i]

    
        return ans
sol = Solution()
ans = sol.convert('A', 2)
print(ans)

